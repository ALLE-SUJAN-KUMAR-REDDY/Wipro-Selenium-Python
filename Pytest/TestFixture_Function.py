# scope is run before and after every function

import pytest

@pytest.fixture("openbrowser")
def test_login():
    print("enter the username")
    print("enter the password")
    print("click on the login button")

@pytest.mark.usefixture("closebrowser")
def test_logout():
    print("User is logged out")




