from src import masks


from src import widget

from src import processing

from src.processing import sorted_list

print(masks.get_mask_card_number("7000792289606361"))

print(masks.get_mask_account("73654108430135874305"))

print(widget.mask_account_card("Visa Platinum 7000792289606361"))

print(widget.mask_account_card("Счет 73654108430135874305"))

print(widget.mask_account_card("MasterCard 7158300734726758"))

print(widget.mask_account_card("Maestro 1596837868705199"))

print(widget.get_date("2024-03-11T02:26:18.671407"))

print(processing.filter_by_state(sorted_list))
