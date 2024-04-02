from classes.abstract_product import AbstractProduct


class Product(AbstractProduct):
    name: str
    desc: str
    price: float
    available: int

    def __init__(self, name: str, desc: str, price: float, available: int):
        self.name = name
        self.desc = desc
        self.__price = price
        self.available = available

    def __add__(self, other):
        if type(other) == self.__class__:
            return self.__price * self.available + other.__price * other.available
        raise TypeError('Нельзя складывать продукты разных типов')

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.available}."

    @classmethod
    def create_product(cls, name, desc, price, available):
        return cls(name, desc, price, available)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price >= 10:
            self.__price = new_price
        else:
            print('Введена некорректная цена')
