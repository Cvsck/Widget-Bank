# Widget-Bank

## Описание:

Проект банковского приложения для работы с пластиковыми картами.

## Установка:

1. Клонируй репозиторий:
'''
 git clone https:// [github.com](https://github.com/Cvsck/Widget-Bank.git)
'''
2. Установка зависимости:
'''
pip install -r requirements.txt
'''
## Тестирование в Readme:
1. Установлена библиотека pytest
'''
poetry add --group dev pytest
'''
2. Сгенерирован отчет о покрытии в HTML-формате
'''
pytest --cov=src --cov-report=html
'''
## Создание нового модуля generators
1. Реализована функция 
'''
filter_by_currency
'''
2. Реализована функция-генератор 
'''
transaction_descriptions
'''
3. Реализован генератор 
'''
card_number_generator
'''
4. Написаны тесты для функций: 
'''
filter_by_currency
'''
transaction_descriptions
'''
'''
card_number_generator
'''