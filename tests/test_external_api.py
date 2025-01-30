from unittest.mock import patch

from src.external_api import currency_conversion

transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8000",
        "currency": {
            "name": "USD",
            "code": "USD"
        }}}


@patch("requests.get")
def test_currency_conversion(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'success': True, 'timestamp': 1720199764, 'base': 'USD',
                                               'date': '2024-07-05',
                                               'rates': {'RUB': 100},'result': 800000.0}
    assert currency_conversion(transaction) == 800000.0