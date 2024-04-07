from classes.abstract_product import AbstractProduct
from classes.print_mixin import PrintMixin


class Product(AbstractProduct, PrintMixin):
    """Базовый класс продукта, от которого будут наследоваться остальные"""
    def __init__(self, name: str, desc: str, price: float, available: int):
        """Инициализатор"""
        self.name = name
        self.desc = desc
        self.__price = price
        self.available = available

    def __add__(self, other):
        """
        Метод для сложения
        Если тип второго слагаемого равен классу Product, то пропускаем
        """
        if self.available == 0:
            raise ValueError('Нельзя складывать товары с нулевым количеством!')
        if type(other) == self.__class__:
            return self.__price * self.available + other.__price * other.available

        raise TypeError('Нельзя складывать продукты разных типов')

    def __str__(self):
        """Строковое представление для пользователя (выводится при print())"""
        return f"{self.name}, {self.price} руб. Остаток: {self.available}."

    @classmethod
    def create_product(cls, name, desc, price, available):
        """Метод, возвращющий объект класса Product"""
        return cls(name, desc, price, available)

    @property
    def price(self):
        """Задаём цену как свойство через декоратор @property"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Так как цена - свойство, можно и сеттер прописать)"""
        if new_price >= 10:
            self.__price = new_price
        else:
            print('Введена некорректная цена')
