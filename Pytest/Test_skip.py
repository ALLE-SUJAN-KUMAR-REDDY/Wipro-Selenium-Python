#skip - if defects are there
# skip - if the testcases are absolute
# windows , mobile - OS dependency
# browsers - FF , IE , chrome

import  pytest

# testcase 1
def testcase1():
    print("Testcase1 is executed")

# testcase 2
@pytest.mark.skip
def testcase2():
    print("Testcase2 is executed")

# testcase 3
def testcase3():
    print("Testcase3 is executed")


# testcase 4
@pytest.mark.skip
def openbrowser():
    print("Openning the browser")