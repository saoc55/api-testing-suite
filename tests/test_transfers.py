class TestTransfers:

    def test_transfers_return_200(self, auth_client, account_id, second_account_id):
        response = auth_client.transfer(account_id, second_account_id, 10.00)
        assert response.status_code == 200

    def test_transfer_reduces_source_balance(self, auth_client, account_id, second_account_id):
        balance_before = auth_client.get_account(account_id).json()["balance"]
        auth_client.transfer(account_id, second_account_id, 10.00)
        balance_after = auth_client.get_account(account_id).json()["balance"]
        assert balance_after < balance_before

    def test_transfer_increases_destination_balance(self, auth_client, account_id, second_account_id):
        balance_before = auth_client.get_account(second_account_id).json()["balance"]
        auth_client.transfer(account_id, second_account_id, 10.00)
        balance_after = auth_client.get_account(second_account_id).json()["balance"]
        assert balance_after > balance_before