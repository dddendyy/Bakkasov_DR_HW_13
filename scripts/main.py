from product import Product
from category import Category

category_attr = ['name', 'desc', 'price', 'available']

if __name__ == '__main__':
    sprite = Product('Sprite', 'carbonated soft drink with lime and lemon flavor', 75, 25)
    pepi = Product('Pepi', 'carbonated soft drink produced by PepsiCo', 99, 49)

    mountain_dew = Product('Mountain Dew',
                           'green drink',
                           129, 10)

    sausage = Product('Sausage',
                      'a food product',
                      259, 70)

    shrimps = Product.create_product('Shrimps', 'So tasty', 369, 29)

    parmegiano = Product('Parmegiano', 'Italian variety of hard cheese of long maturation', 349, 42)

    drinks = Category('Drinks', 'just drink it', [sprite, mountain_dew, pepi])
    food = Category('Food', 'Put it in your mouth and enjoy', [sausage, parmegiano])

    print(sausage)
    print(drinks)
    print(sprite + sausage)


