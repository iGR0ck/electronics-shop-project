from src.item import Item


class Mixin:

    def __init__ (self, name, price, quantity, language="EN"):
        self.language = language
        super().__init__(name, price, quantity)


    def change_lang (self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        return self.language


class Keyboard (Mixin, Item):


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.language})"

    def name(self):
        return super().name

    def change_lang (self):
        Mixin.change_lang(self)
        return self

