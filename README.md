# api-testing-suite

![API Test Suite](https://github.com/saoc55/api-testing-suite/actions/workflows/pytest.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

REST API test suite for [Parabank](https://parabank.parasoft.com) — a banking demo application. Built with Python, Pytest, and Requests as part of a QA automation portfolio.

> Companion project to [playwright-e2e-framework](https://github.com/saoc55/playwright-e2e-framework) — same target app, different layer. E2E UI coverage lives there; API contract coverage lives here.

---

## Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Language |
| Pytest | Test runner |
| Requests | HTTP client |
| pytest-html | Local HTML report |
| GitHub Actions | CI |

---

## Project Structure
api-testing-suite/

├── client/

│   └── parabank_client.py    # Requests wrapper for all API calls

├── tests/

│   ├── conftest.py           # Session-scoped fixtures

│   ├── test_auth.py          # Login / authentication

│   ├── test_accounts.py      # Account retrieval and schema

│   ├── test_transactions.py  # Transaction history

│   └── test_transfers.py     # Fund transfer and balance validation

├── utils/

│   └── test_data.py          # Credentials and test constants

├── .github/workflows/

│   └── pytest.yml            # CI pipeline

└── pytest.ini

---

## Setup

```bash
git clone https://github.com/saoc55/api-testing-suite.git
cd api-testing-suite
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Run Tests

```bash
# Full suite
pytest

# Single module
pytest tests/test_auth.py -v

# HTML report (generated at reports/report.html)
pytest --html=reports/report.html --self-contained-html
```

---

## Test Coverage

| Module | Tests | Endpoint |
|--------|-------|---------|
| Auth | 3 | `GET /login/{username}/{password}` |
| Accounts | 5 | `GET /customers/{id}/accounts`, `GET /accounts/{id}` |
| Transactions | 3 | `GET /accounts/{id}/transactions` |
| Transfers | 3 | `POST /transfer` |
| **Total** | **14** | |

---

## Key Patterns

- **Session-scoped fixtures** — login once per test run, reuse the authenticated client across all modules
- **Schema validation** — field presence checked on all response objects
- **State verification** — transfer tests assert balance changes on both source and destination accounts, not just HTTP 200

---

## License

MIT