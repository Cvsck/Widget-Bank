from src.processing import filter_by_state, list_of_dictionaries, sort_by_date, sorted_list


def test_filter_by_state():
    assert filter_by_state(list_of_dictionaries) == [{'id': 41428829, 'state': 'EXECUTED',
                                                    'date': '2019-07-03T18:35:29.512364'},
                                                    {'id': 939719570, 'state': 'EXECUTED',
                                                    'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date():
    assert sort_by_date(sorted_list) == [{'id': 41428829, 'state': 'EXECUTED',
                                        'date': '2019-07-03T18:35:29.512364'},
                                        {'id': 939719570, 'state': 'EXECUTED',
                                        'date': '2018-06-30T02:08:58.425572'}]
