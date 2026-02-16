# scope is run before and after every function

import pytest

@pytest.fixture()
def test_login(openbrowser):
    print("enter the username")
    print("enter the password")
    print("click on the login button")

@pytest.mark.usefixture()
def test_logout(closebrowser):
    print("User is logged out")




