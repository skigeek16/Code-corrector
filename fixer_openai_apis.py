import os
import re
import subprocess
import time
import json
import requests

# === CONFIGURATION ===
PYTHON_BUGGY_DIR = "python_programs"
PYTHON_FIXED_DIR = "fixed_programs"
PYTHON_TESTCASE_DIR = "python_testcases"
TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
TOGETHER_MODEL = ""#using different models accordingly


os.makedirs(PYTHON_FIXED_DIR, exist_ok=True)

# === AGENT CLASSES ===

class LoaderAgent:
    def load_buggy_code(self, program_name):
        path = os.path.join(PYTHON_BUGGY_DIR, f"{program_name}.py")
        try:
            with open(path, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(f" Buggy code file not found: {path}")
            return None

    def load_test_code(self, program_name):
        # Try exact match
        test_path = os.path.join(PYTHON_TESTCASE_DIR, f"test_{program_name}.py")
        if os.path.exists(test_path):
            with open(test_path, "r") as f:
                return f.read()
        # Try removing '_test' suffix if present
        if program_name.endswith("_test"):
            alt_name = program_name[:-5]
            test_path = os.path.join(PYTHON_TESTCASE_DIR, f"test_{alt_name}.py")
            if os.path.exists(test_path):
                with open(test_path, "r") as f:
                    return f.read()
        return ""

class BugAnalysisAgent:
    def analyze(self, program_name, code):
        prompt = f"""
You are a Python code analyst.

The following function `{program_name}` contains a one-line bug. Identify and explain it.

Return JSON with:
{{
  "line_number": int,
  "buggy_line": str,
  "bug_type": str,
  "explanation": str,
  "fix_suggestion": str
}}

Code:
{code}
"""
        return GPTAgent().call_gpt(prompt)

class PromptAgent:
    def generate_prompt(self, buggy_code, test_code, program_name, analysis):
        output_hint = ""
        pname = program_name.lower()
        if pname == "flatten":
            output_hint = "\nThe function must return a flat list, not a generator or iterator."
        elif pname == "hanoi":
            output_hint = "\nThe function must return a list of moves as tuples, e.g., [(1, 3)], and match test case expectations exactly."
        elif pname == "bitcount":
            output_hint = "\nThe function must be efficient and return an integer count of set bits in binary representation."
        elif pname == "shunting_yard":
            output_hint = "\nThe function must return a list of tokens in Reverse Polish Notation."

        return f"""
You are an expert Python developer.

The following Python function is from a classic algorithm. It contains a one-line bug.
Your task is to fix the bug while preserving the algorithm logic.
Match the expected test case output.
{output_hint}

# Bug Analysis:
{analysis}

# Buggy {program_name}.py:
{buggy_code}

# Test cases:
{test_code}

Return ONLY the corrected code, no explanationand no comments.
"""

class GPTAgent:
    def call_gpt(self, prompt, retries=2):
        url = "https://api.together.xyz/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": TOGETHER_MODEL,
            "messages": [
                {"role": "system", "content": "You are an expert Python developer."},
                {"role": "user", "content": prompt}
            ]
        }
        for attempt in range(retries + 1):
            try:
                response = requests.post(url, headers=headers, json=data, timeout=30)
                response.raise_for_status()
                result = response.json()
                return result["choices"][0]["message"]["content"]
            except Exception as e:
                print(f" Together API call failed (attempt {attempt+1}): {e}")
                if attempt == retries:
                    return ""
                time.sleep(2)

class SaverAgent:
    def save_fixed_code(self, program_name, fixed_code):
        path = os.path.join(PYTHON_FIXED_DIR, f"{program_name}.py")
        try:
            code_only = extract_python_code(fixed_code)
            with open(path, "w") as file:
                file.write(code_only)
        except Exception as e:
            print(f" Failed to save fixed code for {program_name}: {e}")

    def save_bug_report(self, program_name, analysis_json):
        path = f"bug_report_{program_name}.json"
        try:
            with open(path, "w") as f:
                f.write(analysis_json)
        except Exception as e:
            print(f" Failed to save bug report: {e}")

class TestAgent:
    def run_pytest(self, program_name):
        test_file = os.path.join(PYTHON_TESTCASE_DIR, f"test_{program_name}.py")
        if not os.path.exists(test_file):
            print(f" Test case for {program_name} not found at {test_file}.")
            return False, ""
        env = os.environ.copy()
        env["PYTHONPATH"] = f"{os.path.abspath(PYTHON_FIXED_DIR)}:{os.path.abspath(PYTHON_BUGGY_DIR)}:{env.get('PYTHONPATH', '')}"
        try:
            result = subprocess.run(
                ["pytest", test_file, "--maxfail=1", "--disable-warnings", "-q"],
                capture_output=True, text=True, env=env, timeout=60
            )
            passed = "failed" not in result.stdout.lower()
            return passed, result.stdout + "\n" + result.stderr
        except subprocess.TimeoutExpired:
            print(f" Pytest timed out for {program_name}.")
            return False, "Timeout"
        except Exception as e:
            print(f" Pytest execution failed: {e}")
            return False, ""

def extract_python_code(llm_output):
    """
    Extracts only valid Python code from LLM output, removing markdown/code block preambles and explanations.
    Handles common LLM output formats (```python, ```py, ``` etc) and strips leading/trailing whitespace.
    """
    if not llm_output:
        return ""
    # Remove markdown code block markers
    code = re.sub(r"^```(?:python|py)?\\s*", "", llm_output.strip(), flags=re.IGNORECASE)
    code = re.sub(r"```$", "", code.strip())
    # Remove any leading explanations or comments before the first 'def' or 'class' or import
    match = re.search(r"(^|\n)(def |class |import |from )", code)
    if match:
        code = code[match.start(2):]
    return code.strip()

# === MAIN WORKFLOW ===

def main():
    loader = LoaderAgent()
    prompter = PromptAgent()
    gpt = GPTAgent()
    saver = SaverAgent()
    analyzer = BugAnalysisAgent()

    if not os.path.isdir(PYTHON_BUGGY_DIR):
        print(f" Directory '{PYTHON_BUGGY_DIR}' does not exist.")
        return

    all_programs = [f[:-3] for f in os.listdir(PYTHON_BUGGY_DIR) if f.endswith(".py")]
    if not all_programs:
        print(f"No Python programs found in '{PYTHON_BUGGY_DIR}'.")
        return

    for program in all_programs:
        print(f"\nProcessing: {program}")
        buggy_code = loader.load_buggy_code(program)
        if buggy_code is None:
            continue

        print(f"Analyzing bug in {program}...")
        analysis = analyzer.analyze(program, buggy_code)
        print(f"Bug Report: {analysis.strip()[:200]}...")  # Preview
        saver.save_bug_report(program, analysis)

        prompt = prompter.generate_prompt(buggy_code, '', program, analysis)
        fixed_code = gpt.call_gpt(prompt)
        if not fixed_code.strip():
            print(f"Skipping {program} due to empty GPT response.")
            continue

        if program.lower() == "flatten" and "yield" in fixed_code:
            print(f"Wrapping 'flatten' with list(...) to fix generator output.")
            fixed_code = fixed_code.replace("def flatten", "def _flatten_inner", 1)
            fixed_code = (
                "def flatten(*args, **kwargs):\n"
                "    return list(_flatten_inner(*args, **kwargs))\n\n"
            ) + fixed_code

        print(f"Saving fixed code for {program}")
        saver.save_fixed_code(program, fixed_code)
        # No test running or result logging
        time.sleep(60)  # Add a delay of 1 minute between each program

if __name__ == "__main__":
    main()
