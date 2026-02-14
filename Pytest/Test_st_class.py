# used inside the class
# it will run for every class definition 0nce  it will run starting and  at ending of the class
# only method and class work inside the class. Function and class doesn't work

class Testclass1:

    # class level set up
    def setup_class(cls):
        print("API Authorization needed with username and password")

    def teardown_class(cls):
        print("API Authoriztion closed")

    def setup_method(method):
        print("opening the browser")

    def setup_method(method):
        print("closing the browser")

    # testcase 1
    def testcase1(self):
        print("Testcase1 is executed")

    # testcase 2
    def testcase2(self):
        print("Testcase2 is executed")

    # testcase 3
    def testcase3(self):
        print("Testcase3 is executed")

class Testclass2:
    # testcase 1
    def testcase1(self):
        print("Testcase1 is executed")

    # testcase 2
    def testcase2(self):
        print("Testcase2 is executed")

    # testcase 3
    def testcase3(self):
        print("Testcase3 is executed")

