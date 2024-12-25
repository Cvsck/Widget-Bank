import typing


def filter_by_state(my_lists: [str], state: [str] = 'EXECUTED') -> typing.Any:
    """Функция возвращает новый список словарей"""

    new_list_dic = []

    for dat, stat in enumerate(my_lists):
        if stat.get('state') == state:  # основное условия создание нового списка
            new_list_dic.append(stat)

    return new_list_dic


def sort_by_date(new_date: [typing.Any], key: [typing.Any] = None) -> typing.Any:
    """Функция возвращает новый список, отсортированный по дате"""

    if not key:
        key = 'date'  # основное условия создание нового списка
    sorted_data = sorted(new_date, key=lambda x: x.get(key), reverse=True)

    return sorted_data


list_of_dictionaries = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered_list = filter_by_state(list_of_dictionaries, state='EXECUTED')  # аргументы передаются в первую функцию

sorted_list = sort_by_date(filtered_list)  # аргумент принимает вторая функцию на основе полученных данных из первой
