from typing import Union

""" определяем переменную через импорт """


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """ принимает на вход номер карты и возвращает ее маску """

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """ принимает на вход номер счета и возвращает ее маску """

    return f"** {account_number[-4:]}"





