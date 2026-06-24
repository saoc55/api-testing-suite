class TestAccounts:
    
    def test_get_accounts_returns_200(self, auth_client):
        response = auth_client.get_accounts(auth_client.customer_id)
        assert response.status_code == 200
    
    def test_get_accounts_returns_list(self, auth_client):
        response = auth_client.get_accounts(auth_client.customer_id)
        accounts = response.json()
        assert isinstance(accounts, list)
        assert len(accounts)>0

    def test_account_has_required_fields(self, auth_client):
        response = auth_client.get_accounts(auth_client.customer_id)
        account = response.json()[0]
        assert "id" in account
        assert "customerId" in account
        assert "type" in account
        assert "balance" in account
    
    def test_get_account_by_id_returns_200(self, auth_client, account_id):
        response = auth_client.get_account(account_id)
        account = response.json()
        assert response.status_code == 200

    def test_get_account_by_id_matches_id(self, auth_client, account_id):
        response = auth_client.get_account(account_id)
        data = response.json()
        assert data["id"] == account_id

