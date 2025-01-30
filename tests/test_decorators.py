import pytest

from src.decorators import my_function


def test_my_function(capsys):
    """
    Тест проверяет, что `TypeError` действительно выбрасывается,
    и что в выводе содержится ожидаемое сообщение об ошибке
    """
    with pytest.raises(TypeError):
        my_function(2, "3")
    captured = capsys.readouterr()
    assert "my_function error TypeError" in captured.out
