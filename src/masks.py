import logging
from typing import Union

""" определяем переменную через импорт """

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("C:/Users/Макс/my_prj/bank widget/logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """принимает на вход номер карты и возвращает ее маску"""
    logger.info("Начало маскировки карты")
    logger.info("Закончили маскировку карты")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """принимает на вход номер счета и возвращает ее маску"""
    logger.info("Начало маскировки счета")
    logger.info("Закончили маскировку счета")
    return f"** {account_number[-4:]}"
