# fixtures are the piece of the code which are run before the testcases or after the testcases

import pytest



# testcase using the simple fixture
def testcase1(simple_data):
    assert simple_data == 45


def test_api(api_url):
    assert "https" in api_url