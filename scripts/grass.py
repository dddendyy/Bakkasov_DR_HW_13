from product import Product


class Grass(Product):
    """
    Класс Трава газонная, наследуется от базового класса продукта
    имеет доп. поля:
    manufacturer - страна-производитель
    period - период цветения
    color - цвет
    """

    def __init__(self, name: str, desc: str, price: float, available: int, manufacturer: str, period: str, color: str):
        super().__init__(name, desc, price, available)
        self.manufacturer = manufacturer
        self.period = period
        self.color = color
