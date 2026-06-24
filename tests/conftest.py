import pytest
from client.parabank_client import ParabankClient
from utils.test_data import VALID_USER

@pytest.fixture(scope="session")
def client():
    return ParabankClient()

@pytest.fixture(scope="session")
def auth_client():
    c = ParabankClient()
    response = c.login(VALID_USER["username"], VALID_USER["password"])
    assert response.status_code == 200, f"Login failed: {response.text}"
    c.customer_id = response.json()["id"]
    return c

@pytest.fixture(scope="session")
def account_id(auth_client):
    response = auth_client.get_accounts(auth_client.customer_id)
    assert response.status_code == 200
    accounts = response.json()
    assert len(accounts) > 0, "No Accounts foud"
    return accounts[0]["id"]

@pytest.fixture(scope="session")
def second_account_id(auth_client):
    response = auth_client.get_accounts(auth_client.customer_id)
    assert response.status_code == 200
    accounts = response.json()
    assert len(accounts) >= 2, "Need at least 2 accounts for transfer test"
    return accounts[1]["id"]

