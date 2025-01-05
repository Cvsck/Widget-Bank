import pytest


@pytest.fixture
def account_account():
    return "** 4305"


@pytest.fixture
def account_account_1():
    return "** 0546"


@pytest.fixture
def name_number_card():
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def corrected_date():
    return "11.03.2024"
