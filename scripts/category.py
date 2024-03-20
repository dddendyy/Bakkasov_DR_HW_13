class Category:
    name: str
    desc: str
    __goods: list
    goods_count = 0
    categories_count = 0

    def __init__(self, name: str, desc: str, goods: list):
        self.name = name
        self.desc = desc
        self.__goods = goods
        Category.goods_count += len(goods)
        Category.categories_count += 1
        self.categories_count = Category.categories_count
        self.goods_count = Category.goods_count

    def add_goods(self, value):
        self.__goods.append(value)

    @property
    def goods(self):
        '''декоратор для форматного вывода товаров'''
        output = ''
        for good in self.__goods:
            output += f"{good.name}, {good.price} руб. Остаток: {good.available}\n"

        return output
