import pytest
from load_testdata import load_json_testcases

if pytest.fixed:
    from fixed_programs.sqrt import sqrt
elif pytest.use_correct:
    from correct_python_programs.sqrt import sqrt
else:
    from python_programs.sqrt import sqrt

testdata = load_json_testcases(sqrt.__name__)

@pytest.mark.parametrize("input_data,expected", testdata)
def test_sqrt(input_data, expected):
    assert sqrt(*input_data) == expected