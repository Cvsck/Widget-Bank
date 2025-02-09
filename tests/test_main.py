import unittest
from unittest.mock import mock_open, patch

from main import filter_by_state, get_amount, main, read_file_json


# Тест для функции read_file_json
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"date": "2020-01-19T16:23:39Z", "description": "Открытие вклада",'
              ' "to": "Счет **4321", "operationAmount": {"amount": 40542, "currency": {"code": "RUB"}}, '
              '"state": "EXECUTED"}]',
)
def test_read_file_json(mock_file):
    result = read_file_json("dummy_path")
    assert result == [
        {
            "date": "2020-01-19T16:23:39Z",
            "description": "Открытие вклада",
            "to": "Счет **4321",
            "operationAmount": {"amount": 40542, "currency": {"code": "RUB"}},
            "state": "EXECUTED",
        }
    ]


# Тест для функции filter_by_state
def test_filter_by_state():
    transactions = [{"state": "EXECUTED"}, {"state": "PENDING"}]
    result = filter_by_state(transactions, "EXECUTED")
    assert result == [{"state": "EXECUTED"}]


# Тест для функции get_amount
def test_get_amount():
    transaction = {"operationAmount": {"amount": 40542}}
    result = get_amount(transaction)
    assert result == 40542


# Тест для основной функции main
@patch("builtins.input", side_effect=["1", "EXECUTED", "да", "по возрастанию", "нет", "нет"])
@patch(
    "src.main.read_file_json",
    return_value=[
        {
            "date": "2020-01-19T16:23:39Z",
            "description": "Открытие вклада",
            "to": "Счет **4321",
            "operationAmount": {"amount": 40542, "currency": {"code": "RUB"}},
            "state": "EXECUTED",
        }
    ],
)
@patch("builtins.print")
def test_main(mock_print, mock_read_file_json, mock_input):
    main()
    mock_print.assert_any_call("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    mock_print.assert_any_call("Для обработки выбран JSON-файл")
    mock_print.assert_any_call("Распечатываю итоговый список транзакций...\nВсего банковских операций в выборке: 1\n")
    mock_print.assert_any_call("19.01.2020 Открытие вклада\nСчет **4321\nСумма: 40542 RUB.\n")


if __name__ == "__main__":
    unittest.main()
