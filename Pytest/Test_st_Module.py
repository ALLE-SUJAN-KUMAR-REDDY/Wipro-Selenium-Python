# module level - runs once per module (file)
# use module level set up and tear down when you want to execute the set up and tear down once in the current file
# eg open the db connection execute all the testcases and at alst close the db connection

# setup_module - -> only one per class
# setup_class() -> one per class
# setup_method() -> one per class
# set_function() -> one per class


import  pytest
def setup_module(module):
    print("Open the db connection")
    print("Navigating to home page")

def teardown_module(module):
    print("Closing the db connection")

# testcase 1
def read():
    print("Reading the db")

# testcase 2
def write():
    print("Writing the data to the db")

# testcase 3
def test_updating():
    print("updating the db")

