# basic assertion
import pytest_check as check

# hard assertions - this will stop the execution of the test case / test suite
# soft assertions will continue to run even if the assertion fails

# basic assertion
def test_add():
    result = 2 + 3
    assert result == 5


# checking true or false
def test_boolean():
    assert True
    assert not False

# none value

def test_none():
    value = None
    assert value is None

# list assertion
def test_list():
    fruits = ["apple", "banana", "orange"]
    assert "banana" in fruits

# Dict assertion
def test_list():
    creds = {"username" : "admin", "password":"admin123"}
    assert creds["password"] == "admin123"

# comparing lists
def test_comparelist():
    assert [1,2,3] == [1,2,3]

# assertion with custom message

def test_custommsg():
    result = 10
    assert result == 10, "Result should be 5"

# soft

def test_multiple():
    check.equal(1,2)
    check.equal(3,3)
