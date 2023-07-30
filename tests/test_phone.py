import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_сlass_phone_iphone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_attributes (test_сlass_phone_iphone):

    phone1 = test_сlass_phone_iphone
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120000
    assert phone1.quantity == 5


def test_sims_more_zero ():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)

    with pytest.raises(ValueError):
        phone1.number_of_sim = 0

def test_add_in_phone (test_сlass_phone_iphone):

    class Test_cls:
        def __init__(self, quantity: int):
            self.quantity = quantity

    test_ex = Test_cls (5)
    item1 = Item("Смартфон", 10000, 20)
    phone1 = test_сlass_phone_iphone

    assert phone1 + phone1 == 10
    assert phone1 + test_ex == "Эти экземпляры нельзя сложить"
    assert phone1 + item1 == 25
    assert phone1 + 10 == "Эти экземпляры нельзя сложить"
