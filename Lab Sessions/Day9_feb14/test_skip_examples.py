# 1.Write a test that is skipped because a feature is not implemented yet.

import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_new_feature():
    assert True

# 2.write a test that runs only on Linux and skips on Windows.

import pytest
import sys

@pytest.mark.skipif(sys.platform == "win32", reason="Runs only on Linux")
def test_linux_only_feature():
    assert True

# 3.Write a test that checks an API health endpoint. If status code is not 200 → skip the test dynamically.

import pytest
import requests

def test_api_health():
    response = requests.get("https://httpbin.org/status/200")

    if response.status_code != 200:
        pytest.skip("API is not healthy")

    assert response.status_code == 200

# 4.Mark a failing test as xfail with reason: "Bug #123".

import pytest

@pytest.mark.xfail(reason="Bug #123")
def test_known_bug():
    assert 1 == 2

# 5. You have 5 parameterized cases 2 are known bugs. Mark only those 2 cases as xfail without marking entire test.

import pytest

@pytest.mark.parametrize(
    "input_value, expected",
    [
        (2, 4),  # pass
        (3, 9),  # pass
        pytest.param(4, 15, marks=pytest.mark.xfail(reason="Bug #101")),  # known bug
        pytest.param(5, 20, marks=pytest.mark.xfail(reason="Bug #102")),  # known bug
        (6, 36),  # pass
    ]
)
def test_square(input_value, expected):
    assert input_value * input_value == expected
