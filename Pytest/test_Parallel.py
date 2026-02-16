import  pytest
from Test_SimpleFixture1 import api_url
# testcase 1
def testcase1():
    print("Testcase1 is executed")

# testcase 2
def testcase2():
    print("Testcase2 is executed")

# testcase 3
def testcase3():
    print("Testcase3 is executed")

# testcase 4
def testcase4():
    print("Testcase4 is executed")

# testcase 5
def testcase5():
    print("Testcase5 is executed")
def test_logi():
    print("Login test is executed")
def test_api(api_url):
    assert "https" in api_url
