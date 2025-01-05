import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize('number, expected', [("7000792289606361", "7000 79** **** 6361"),
                                              ("7158300734726758", "7158 30** **** 6758"),
                                              ("7108300734726956", "7108 30** **** 6956"),
                                              ("710830070000034726956", "7108 30** **** 6956")],)


def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected

    with pytest.raises(TypeError):
        get_mask_card_number(number="fddf31231313dvd", expected="0")


def test_get_mask_account(account_account):
    assert get_mask_account("73654108430135874305") == account_account


def test_get_mask_account_length(account_account_1):
    assert get_mask_account("7365410843013587430546") == account_account_1
