# 1. Write a pytest fixture that generates an authentication token once per session and use it in multiple API test cases.

def test_auth_token(auth_token):
    print("\nUsing auth token:", auth_token)
    assert auth_token == "dummy_token"

