import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name    #lesson 2
        self.price = price
        self.quantity = quantity

    #класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
    # путь к файлу менять вручную, при использовании os path или коротком пути выдавало ошибку FileNotFoundError
    @classmethod
    def instantiate_from_csv(cls):
        with open('/Users/igorpetushkov/PycharmProjects/electronics-shop-project/src/items.csv', newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            Item.all = []
            for row in reader:
                Item.all.append(Item(row['name'], row['price'], row['quantity']))
        return Item.all

    # lesson 2
    @property
    def name(self):
        return self.__name

        # lesson 2
    @name.setter
    def name(self, item_name):
        self.__name = item_name
        if len(self.__name) > 10:
            self.__name = self.__name[0:9]


    #статический метод, возвращающий число из числа-строки
    @staticmethod
    def string_to_number(number: str):
        int_number = int(float(number))
        return int_number



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        discount = self.price * Item.pay_rate
        self.price = discount
        return self.price




