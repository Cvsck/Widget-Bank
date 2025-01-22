import pytest

from src.decorators import my_function


def test_my_function(capsys):
    my_function(2, "3")
    captured = capsys.readouterr()
    assert captured.out == "f{func.__name__} error {e.__class__.__name__}.Inputs: {args}, {kwargs}"
