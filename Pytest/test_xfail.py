#xfail is a marker used to indicate that a test is expected to fail due to known issue
from email.policy import strict

import pytest
import reason
import sys


@pytest.mark.xfail(reason="Known bug in the third-party library")
def test_function_that_fails():
    assert 1 + 1 == 3 # This assertion will fail, but the test suite won't break

# testcase 1
@pytest.mark.sanity
def testcase1():
    print("Testcase1 is executed")

# testcase 2
@pytest.mark.regression
def testcase2():
    print("Testcase2 is executed")

# testcase 3
@pytest.mark.db
def testcase3():
    print("Testcase3 is executed")


# xfail with a condition
@pytest.mark.xfail(sys.platform == "win32" , reason="Bug on windows")
def test():
    print("test on windows")

# this xfail will fail only on windows

# strict=True XFAIL FAILED Fails the test suite
@pytest.mark.xfail(strict=True, reason="Bug #1234 is not fixed yet")
def test_fuction():
    assert  True

# the testcase should fail manadatorily
