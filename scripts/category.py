class Category:
    name: str
    desc: str
    goods: list
    goods_count = 0
    categories_count = 0

    def __init__(self, name: str, desc: str, goods: list):
        self.name = name
        self.desc = desc
        self.goods = goods
        Category.goods_count += len(set(goods))
        Category.categories_count += 1
        self.categories_count = Category.categories_count
        self.goods_count = Category.goods_count
