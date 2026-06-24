import requests

BASE_URL = "https://parabank.parasoft.com/parabank/services/bank"

class ParabankClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})
        self.customer_id = None

    def login(self, username, password):
        return self.session.get(f"{BASE_URL}/login/{username}/{password}")
    
    def get_account(self, account_id):
        return self.session.get(f"{BASE_URL}/accounts/{account_id}")
    
    def get_accounts(self, customer_id):
        return self.session.get(f"{BASE_URL}/customers/{customer_id}/accounts")
    
    def get_transactions(self, account_id):
        return self.session.get(f"{BASE_URL}/accounts/{account_id}/transactions")
    
    def transfer(self, from_account_id, to_account_id, amount):
        return self.session.post(f"{BASE_URL}/transfer", params = {
            "fromAccountId": from_account_id,
            "toAccountId": to_account_id,
            "amount": amount
        }) 
    
    def request_loan(self, customer_id, from_account_id, loan_amount, down_payment):
        return self.session.post(f"{BASE_URL}/requestLoan", params={
            "customeId": customer_id,
            "fromAccountId": from_account_id,
            "loanAmount": loan_amount,
            "downPayment": down_payment

        })
    
