# 3. Write a test that validates JSON response schema from an API endpoint.

def test_user_response_schema():
    # Mocked API response
    response = {
        "id": 1,
        "name": "John",
        "email": "john@test.com",
        "is_active": True
    }

    # Validate schema (keys)
    assert "id" in response
    assert "name" in response
    assert "email" in response
    assert "is_active" in response

    # Validate data types
    assert isinstance(response["id"], int)
    assert isinstance(response["name"], str)
    assert isinstance(response["email"], str)
    assert isinstance(response["is_active"], bool)
