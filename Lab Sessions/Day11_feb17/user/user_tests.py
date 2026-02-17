# 2. Create a fixture that creates a test user via API before a test and deletes the user after test execution using yield.

def test_user_flow(auth_token, test_user):
    assert auth_token == "dummy_token"
    assert test_user == 101

def test_user_flow(base_url, auth_token, user):
    print("test running")
    assert user == 101
