"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone




@pytest.fixture
def test_class_item_apple():
    return Item('Яблоко', 30, 60)

def test_init_class_item (test_class_item_apple):
    """
    Проверка метода __init__
    """
    assert test_class_item_apple.name == "Яблоко"
    assert test_class_item_apple.price == 30
    assert test_class_item_apple.quantity == 60


def test_calculate_price (test_class_item_apple):
    """
    Проверка подсчёта общей стоимости товара
    """
    result = test_class_item_apple.calculate_total_price()
    assert result == 1800


def test_discount_price (test_class_item_apple):
    """
    Проверка функции расчёта скидки
    """
    test_class_item_apple.apply_discount()
    result = test_class_item_apple.price
    return result == 30


# lesson 2
def test_property_name (test_class_item_apple):
    test_class_item_apple.name = "Можжевельник"
    assert test_class_item_apple.name == "Можжевель"


def test_string_to_number (test_class_item_apple):
    assert test_class_item_apple.string_to_number('5') == 5
    assert test_class_item_apple.string_to_number('5.0') == 5
    assert test_class_item_apple.string_to_number('5.5') == 5


def test_instantiate_from_csv ():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_repr_for_item_class ():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str_for_item_class ():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == 'Смартфон'


def test_add_in_Item ():
    class Test_cls:
        def __init__(self, quantity: int):
            self.quantity = quantity

    test_ex = Test_cls (5)
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)

    assert item1 + item1 == 40
    assert item1 + test_ex == "Эти экземпляры нельзя сложить"
    assert item1 + phone1 == 25
    assert item1 + 10 == "Эти экземпляры нельзя сложить"
