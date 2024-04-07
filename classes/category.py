from classes.product import Product

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

    def __len__(self):
        return len(self.__goods)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def add_goods(self, value):
        if isinstance(value, Product):
            self.__goods.append(value)
        else:
            raise TypeError("Нельзя к продукту добавлять левые объекты!")

    @property
    def goods(self):
        """декоратор для форматного вывода товаров"""
        output = ''
        for good in self.__goods:
            output += f"{good.name}, {float(good.price)} руб. Остаток: {good.available}\n"

        return output

    def average(self):
        """
        Функия для поиски среднего ценника всех продуктов
        """
        goods_sum = 0
        try:
            for good in self.__goods:
                goods_sum += good.price
            result = goods_sum / len(self.__goods)
            return result
        except ZeroDivisionError:
            return 0
