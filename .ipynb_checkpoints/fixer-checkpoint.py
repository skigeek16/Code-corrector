import os
import subprocess
import time
import openai

# ========== CONFIG ==========
openai.api_key = os.getenv("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")
openai.api_base = "https://api.groq.com/openai/v1"

PYTHON_BUGGY_DIR = "python_programs"
PYTHON_FIXED_DIR = "fixed_programs"
PYTHON_TESTCASE_DIR = "python_testcases"
# ============================

os.makedirs(PYTHON_FIXED_DIR, exist_ok=True)

def load_buggy_code(program_name):
    path = os.path.join(PYTHON_BUGGY_DIR, f"{program_name}.py")
    with open(path, "r") as file:
        return file.read()

def generate_prompt(buggy_code, program_name):
    return f"""
You are an expert Python developer.

The following Python function is from a well-known algorithm but contains a one-line bug. 
Please fix the bug and return the full corrected function with the same name and parameters.

# Buggy {program_name}.py:
{buggy_code}
"""

def call_gpt(prompt):
    print("⏳ Calling Groq GPT")
    try:
        response = openai.ChatCompletion.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(f"❌ GPT API call failed: {e}")
        return ""

def save_fixed_code(program_name, fixed_code):
    path = os.path.join(PYTHON_FIXED_DIR, f"{program_name}.py")
    with open(path, "w") as file:
        file.write(fixed_code)

def run_pytest(program_name):
    test_file = os.path.join(PYTHON_TESTCASE_DIR, f"test_{program_name}.py")
    if not os.path.exists(test_file):
        print(f"❌ Test case for {program_name} not found.")
        return False, ""
    env = os.environ.copy()
    env["PYTHONPATH"] = PYTHON_FIXED_DIR
    result = subprocess.run(
        ["pytest", test_file, "--maxfail=1", "--disable-warnings", "-q"],
        capture_output=True, text=True, env=env
    )
    passed = "failed" not in result.stdout.lower()
    return passed, result.stdout

def main():
    all_programs = [f[:-3] for f in os.listdir(PYTHON_BUGGY_DIR) if f.endswith(".py")]
    success_count = 0

    for program in all_programs:
        print(f"\n🔍 Processing: {program}")
        buggy_code = load_buggy_code(program)
        prompt = generate_prompt(buggy_code, program)
        fixed_code = call_gpt(prompt)

        if not fixed_code.strip():
            print(f"⚠️ Skipping {program} due to empty GPT response.")
            continue

        save_fixed_code(program, fixed_code)
        passed, output = run_pytest(program)
        if passed:
            print(f"✅ {program}: Passed all tests.")
            success_count += 1
        else:
            print(f"❌ {program}: Test failed.")
            print(output)

        time.sleep(1)

    print(f"\n🎯 Success Rate: {success_count}/{len(all_programs)}")

if __name__ == "__main__":
    main()
