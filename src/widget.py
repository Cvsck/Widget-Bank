from typing import Union

""" определяем переменную через импорт """

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(mac_number: Union[str, int]) -> Union[str]:
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


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Maestro 1596837868705199"))


def get_date(day_number: Union[str, int]) -> str:
    """Функция возвращает дату операции"""

    return ".".join(day_number[:10].replace("-", ".").replace(":", "").split("."))


new_date = get_date("2024-03-11T02:26:18.671407").split('.')
result_date = ".".join(new_date[::-1])
print(result_date)
