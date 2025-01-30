from src.widget import mask_account_card, get_date


def test_mask_account_card(name_number_card):
    assert mask_account_card("Visa Platinum 7000792289606361") == name_number_card


def test_get_date(corrected_date):
    assert get_date("2024-03-11T02:26:18.671407") == corrected_date
