import pytest

@pytest.fixture
def user(auth_token):
    print("user created")
    user_id = 101
    yield user_id
    print("user deleted")
