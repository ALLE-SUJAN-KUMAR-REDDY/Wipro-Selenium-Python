import pytest

# request - pytest object that contains information about
# who is calling the fixture and with what data



def testbrowser(browser):
    assert browser in ["chrome", "firefox"]

# Selecting even or odd

import pytest

@pytest.fixture(params=[2, 3, 4, 7])
def number(request):
    return request.param

@pytest.mark.parametrize("expected", ["Even", "Odd"])
def test_even_or_odd(number, expected):
    result = "Even" if number % 2 == 0 else "Odd"
    assert result in ["Even", "Odd"]
