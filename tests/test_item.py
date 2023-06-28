"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def test_ClassItem_Apple():
    return Item('Яблоко', 30, 60)

def test_init_ClassItem (test_ClassItem_Apple):
    """
    Проверка метода __init__
    """
    assert test_ClassItem_Apple.name == "Яблоко"
    assert test_ClassItem_Apple.price == 30
    assert test_ClassItem_Apple.quantity == 60


def test_calculate_price (test_ClassItem_Apple):
    """
    Проверка подсчёта общей стоимости товара
    """
    result = test_ClassItem_Apple.calculate_total_price()
    assert result == 1800


def test_discount_price (test_ClassItem_Apple):
    """
    Проверка функции расчёта скидки
    """
    result = test_ClassItem_Apple.apply_discount()
    return result == 30