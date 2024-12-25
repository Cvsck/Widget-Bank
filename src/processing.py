from typing import List, Any


def filter_by_state(my_lists, state='EXECUTED') -> Any:
    new_list = []

    for dat, stat in enumerate(my_lists):
        if stat.get('state') == state:
            new_list.append(stat)

    return new_list


def sort_by_date(new_date, key=None) -> Any:
    if not key:
        key = 'date'
    sorted_data = sorted(new_date, key=lambda x: x.get(key), reverse=True)

    return sorted_data


my_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered_list = filter_by_state(my_list, state='EXECUTED')
sorted_list = sort_by_date(filtered_list)

print(sorted_list)
