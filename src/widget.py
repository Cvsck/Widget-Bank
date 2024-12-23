from typing import Union

""" определяем переменную через импорт """

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(mac_number: Union[str]) -> str:
    """  Функция принимает список  """
    name_card = ''
    number_card = ''
    number_account = 0
    for i in mac_number:
        if i.isalpha():
            name_card += i  # добавляет если значение буква в пустую строку
        elif i.isdigit():
            number_card += str(i)  # добавляет если значение цифра в пустую строку
            number_account += 1

    if number_account > 16:
        return f"{name_card} {get_mask_account(number_card)}"
    elif name_card == "VisaPlatinum":
        return f"{name_card[0:4]} {name_card[4:]} {get_mask_card_number(number_card)}"
    else:
        return f"{name_card} {get_mask_card_number(number_card)}"


def get_date(day_number: Union[str]) -> str:
    """Функция возвращает дату операции"""
    new_date = day_number[:10].split('-')
    result_date = ".".join(new_date[::-1])  # получаем обратный порядок
    return result_date
    # объединяет элементы списка обратно в строку
