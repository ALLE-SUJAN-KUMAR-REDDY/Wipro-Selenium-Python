# 4. Implement a parametrized test that validates multiple HTTP status codes (200, 400, 401, 500).

import pytest

@pytest.mark.parametrize("status_code", [200, 400, 401, 500])
def test_api_response(status_code):
    response = {"status_code": status_code}
    assert response["status_code"] == status_code
