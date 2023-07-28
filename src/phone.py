from src.item import Item


class Phone(Item):
    
    def __init__(self, name, price, quantity, number_of_sim: int):
        
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', " \
               f"{self.price}, {self.quantity}, " \
               f"{self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        if int(number) and number > 0:
            self.__number_of_sim = number
            return self.__number_of_sim
        else:
            raise ValueError

