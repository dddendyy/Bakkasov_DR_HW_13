from product import Product
from category import Category

category_attr = ['name', 'desc', 'price', 'available']

if __name__ == '__main__':
    sprite = Product('Sprite', 'carbonated soft drink with lime and lemon flavor', 75, 25)

    pepi = Product('Pepi', 'carbonated soft drink produced by PepsiCo', 99, 49)

    mountain_dew = Product('Mountain Dew',
                           'a refreshing green drink that has a rich, pronounced citrus taste and a pleasant aroma',
                           129, 10)

    sausage = Product('Sausage',
                      'a food product; a class-forming type of sausage products, which is minced meat in an oblong shell',
                      259, 70)

    parmegiano = Product('Parmegiano', 'Italian variety of hard cheese of long maturation', 349, 42)

    drinks = Category('Drinks', 'just drink it', [dict(zip(category_attr, (sprite.name, sprite.desc, sprite.price, sprite.available))),
                                                dict(zip(category_attr, (pepi.name, pepi.desc, pepi.price, pepi.available))),
                                                 dict(zip(category_attr, (mountain_dew.name, mountain_dew.desc, mountain_dew.price, mountain_dew.available)))])

    food = Category('Food', 'Put it in your mouth and enjoy', [dict(zip(category_attr, (parmegiano.name, parmegiano.desc, parmegiano.price, parmegiano.available))),
                                                              dict(zip(category_attr, (sausage.name, sausage.desc, sausage.price, sausage.available)))])

    print(drinks.goods)
    print(food.goods)