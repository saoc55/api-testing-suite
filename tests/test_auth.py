from client.parabank_client import ParabankClient
from utils.test_data import VALID_USER, INVALID_USER

class TestAuth:

    def test_valid_login_return_200(self, client):
        response = client.login(VALID_USER["username"], VALID_USER["password"])
        assert response.status_code == 200

    def test_valid_login_return_customer_id(self, client):
        response = client.login(VALID_USER["username"], VALID_USER["password"])
        data = response.json()
        assert "id" in data
        assert data["id"] is not None

    def test_invalid_login_is_rejected(self, client):
        response = client.login(INVALID_USER["username"], INVALID_USER["password"])
        assert response.status_code != 200

    