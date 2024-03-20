class Product:
    name: str
    desc: str
    price: float
    available: int

    def __init__(self, name: str, desc: str, price: float, available: int):
        self.name = name
        self.desc = desc
        self.__price = price
        self.available = available

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
