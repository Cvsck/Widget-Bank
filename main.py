import json
import os
import re
from collections import Counter

from src import masks, processing, widget
from src.CSV_Excel import read_csv, read_excel
from src.processing import sorted_list
from src.widget import get_date, mask_account_card


def read_file_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def search_transactions_by_description(transactions, search_string):
    """
    Функция для поиска операций по заданной строке в описании.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]


def count_transactions_by_category(transactions):
    """
    Функция для подсчета количества операций по категориям.
    """
    categories = [transaction["description"] for transaction in transactions]
    return dict(Counter(categories))


def filter_by_state(operations, status):
    return [t for t in operations if isinstance(t.get("state", ""), str) and t.get("state", "").upper() == status]


def filter_by_currency(transactions, currency_code):
    filtered_transactions = [
        t for t in transactions if t.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
    ]
    print(f"Фильтруем транзакции по валюте: {currency_code}, найдено {len(filtered_transactions)} транзакций")
    return filtered_transactions


def get_amount(transaction):
    """
    Функция для получения суммы транзакции, независимо от структуры данных.
    """
    amount_keys = [
        ["operationAmount", "amount"],
        ["amount"],
        ["value"],
        # Добавьте другие ключи здесь, если нужно
    ]
    for keys in amount_keys:
        value = transaction
        try:
            for key in keys:
                value = value[key]
            return value
        except KeyError:
            continue
    return "не указана"


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    work_file = input("Ваш выбор: ").strip()

    while True:
        if work_file == "1":
            print("Для обработки выбран JSON-файл")
            read_file = read_file_json(os.path.join(os.path.dirname(__file__), "data/operations.json"))
            break
        elif work_file == "2":
            print("Для обработки выбран CSV-файл")
            read_file = read_csv("C:\\Users\\Макс\\my_prj\\bank widget\\transactions.csv")
            break
        elif work_file == "3":
            print("Для обработки выбран XLSX-файл")
            read_file = read_excel("C:\\Users\\Макс\\my_prj\\bank widget\\transactions_excel.xlsx")
            break
        else:
            work_file = input("Данного варианта нет в списке, попробуйте еще раз:\nВаш выбор: ").strip()

    status_operation = (
        input(
            "\nВведите статус, по которому необходимо выполнить фильтрацию. "
            "\nДоступные для фильтрации статусы: EXECUTED, CANCELED, PENDING:\nВвод: "
        )
        .strip()
        .upper()
    )

    while True:
        if status_operation in {"EXECUTED", "CANCELED", "PENDING"}:
            status_operation_filter = filter_by_state(read_file, status_operation)
            break
        else:
            status_operation = (
                input(
                    f"Статус {status_operation} не доступен.\n"
                    "\nВведите статус, по которому необходимо выполнить фильтрацию."
                    "\nДоступные для фильтрации статусы: EXECUTED, CANCELED, PENDING:\nВвод: "
                )
                .strip()
                .upper()
            )

    while True:
        question_sort_data = input("Отсортировать операции по дате? Да/Нет\nВаш выбор: ").lower()
        if question_sort_data == "да":
            question_sort_data_reverse = (
                input("Отсортировать по возрастанию или по убыванию?\nВаш выбор: ").strip().lower()
            )
            reverse = question_sort_data_reverse == "по убыванию"
            status_operation_filter.sort(key=lambda t: t.get("date", ""), reverse=reverse)
            break
        elif question_sort_data == "нет":
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз:")

    while True:
        question_currency = input("Выводить транзакции по определенной валюте? Да/Нет\nВаш выбор: ").lower()
        if question_currency == "да":
            currency_code = input("Введите код валюты (например, RUB, USD): ").strip().upper()
            status_operation_filter = filter_by_currency(status_operation_filter, currency_code)
            break
        elif question_currency == "нет":
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз:")

    while True:
        question_description = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nВаш выбор: "
        ).lower()
        if question_description == "да":
            search_string = input("Введите строку поиска: ").strip()
            finaly_filter = search_transactions_by_description(status_operation_filter, search_string)
            break
        elif question_description == "нет":
            finaly_filter = status_operation_filter
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз:")

    print(f"Распечатываю итоговый список транзакций...\nВсего банковских операций в выборке: {len(finaly_filter)}\n")
    if finaly_filter:
        for trans in finaly_filter:
            amount = get_amount(trans)
            currency = trans.get("operationAmount", {}).get("currency", {}).get("code", "не указана")
            if "Открытие вклада" in trans["description"]:
                print(
                    f"{get_date(trans['date'])} Открытие вклада\n{mask_account_card(trans['to'])}"
                    f"\nСумма: {amount} {currency}.\n"
                )
            else:
                print(
                    f"{get_date(trans['date'])} {trans['description']}\n{mask_account_card(trans['from'])} -> "
                    f"{mask_account_card(trans['to'])}\nСумма: {amount} {currency}.\n"
                )
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()


print(masks.get_mask_card_number("7000792289606361"))

print(masks.get_mask_account("73654108430135874305"))

print(widget.get_mask_card_number("Visa Platinum 7000792289606361"))

print(widget.get_mask_card_number("Счет 73654108430135874305"))

print(widget.get_mask_card_number("MasterCard 7158300734726758"))

print(widget.get_mask_card_number("Maestro 1596837868705199"))

print(widget.get_date("2024-03-11T02:26:18.671407"))

print(processing.filter_by_state(sorted_list))
