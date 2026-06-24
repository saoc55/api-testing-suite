class TestTransactions:

    def test_get_transactions_returns_200(self, auth_client, account_id):
        response = auth_client.get_transactions(account_id)
        assert response.status_code == 200

    def test_get_transactions_returns_list(self, auth_client, account_id):
        response = auth_client.get_transactions(account_id)
        data = response.json()
        assert isinstance(data, list)

    def test_get_transactions_has_required_fields(self, auth_client, account_id):
        response = auth_client.get_transactions(account_id)
        transactions = response.json()
        if len(transactions)>0:
            t = transactions[0]
            assert "id" in t
            assert "accountId" in t
            assert "amount" in t
            assert "type" in t
            assert "date" in t
            