class Product:
    name: str
    desc: str
    price: float
    available: int

    def __init__(self, name, desc, price, available):
        self.name = name
        self.desc = desc
        self.price = price
        self.available = available