from classes.product import Product


class Smartphone(Product):
    """
    Класс смартфон, наследуется от базового класса продукта
    имеет доп. поля:
    perfomance - производительность (частота процессора в ГГц)
    model - модель
    memory - объем памяти (количество ГБ)
    color - цвет
    """
    def __init__(self, name: str, desc: str, price: float, available: int, perfomance: float, model: str, memory: int, color: str):
        super().__init__(name, desc, price, available)
        self.perfomance = perfomance
        self.model = model
        self.memory = memory
        self.color = color
