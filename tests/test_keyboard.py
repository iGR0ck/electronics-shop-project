import pytest

from src.keyboard import Keyboard


@pytest.fixture
def test_class_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init_class_keyboard (test_class_keyboard):
    """
    Проверка метода __init__
    """
    assert test_class_keyboard.name == "Dark Project KD87A"
    assert test_class_keyboard.price == 9600
    assert test_class_keyboard.quantity == 5
    assert test_class_keyboard.language == "EN"


def test_repr_for_item_class (test_class_keyboard):
    kb = test_class_keyboard
    assert repr(kb) == "Keyboard('Dark Project KD87A', 9600, 5, EN)"


def test_keyboard_change_lang (test_class_keyboard):
    kb = test_class_keyboard

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"