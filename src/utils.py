import json
import logging
import os
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("C:/Users/Макс/my_prj/bank widget/logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_financial_transactions(path: str) -> list[Any] | Any:
    """
    Функция принимающая путь к файлу, считывает информацию c JSON файла
    """
    if not os.path.exists(path):
        logger.error("Файл не найден")
        return []  # В случае ошибки возвращает пустой список
    logger.info("Начало загрузки JSON файла")
    with open(path, encoding="utf-8") as file_json:
        data_json = json.load(file_json)
    return data_json


transactions = get_financial_transactions("C:\\Users\\Макс\\my_prj\\bank widget\\data\\operations.json")

print(transactions)
