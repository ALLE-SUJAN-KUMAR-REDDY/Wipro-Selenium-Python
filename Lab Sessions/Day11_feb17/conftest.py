import pytest

@pytest.fixture
def base_url():
    print("base_url created")
    return "https://api.example.com"

@pytest.fixture
def auth_token(base_url):
    print("auth_token created")
    return "dummy_token"
