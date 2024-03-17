class Category:
    name: str
    desc: str
    goods: list
    goods_count: int
    categories_count = 0

    def __init__(self, name, desc, goods):
        self.name = name
        self.desc = desc
        self.goods = goods
        self.goods_count = len(set(goods))
        Category.categories_count += 1
        self.categories_count = Category.categories_count


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

sprite = Product('Sprite', 'carbonated soft drink with lime and lemon flavor', 75, 25)
pepi = Product('Pepi', 'carbonated soft drink produced by PepsiCo', 99, 49)
mountain_dew = Product('Mountain Dew', 'a refreshing green drink that has a rich, pronounced citrus taste and a pleasant aroma', 129, 10)
sausage = Product('Sausage', 'a food product; a class-forming type of sausage products, which is minced meat in an oblong shell', 259, 70)
parmegiano = Product('Parmegiano', 'Italian variety of hard cheese of long maturation', 349, 42)


drinks = Category('Drinks', 'just drink it', [sprite.name, pepi.name, mountain_dew.name])
food = Category('Food', 'Put it in your mouth and enjoy', [sausage.name, parmegiano.name])
