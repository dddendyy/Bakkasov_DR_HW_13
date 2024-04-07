from classes.product import Product
from classes.category import Category
from classes.smartphone import Smartphone

if __name__ == '__main__':
    sprite = Product('Sprite', 'carbonated soft drink with lime and lemon flavor', 75, 25)
    pepi = Product('Pepi', 'carbonated soft drink produced by PepsiCo', 99, 49)
    mountain_dew = Product('Mountain Dew','green drink',3, 10)

    sausage = Product('Sausage','a food product',259, 70)
    shrimps = Product.create_product('Shrimps', 'So tasty', 369, 29)
    parmegiano = Product('Parmegiano', 'Italian variety of hard cheese of long maturation', 349, 42)

    iphone_11 = Smartphone('Apple', 'Device with bited apple', 160_000, 10, 2.65, 'iPhone 11', 256, 'Black')
    redmi_note_11 = Smartphone('Xiaomi', 'Cheap but good device', 35_000, 35, 2.0, 'Redmi Note 11', 128, 'Grey')
    samsung_galaxy = Smartphone('Samsung', 'Nice camera', 56_999, 20, 2.55, 'Galaxy S3', 128, 'Black')

    drinks = Category('Drinks', 'just drink it', [sprite, mountain_dew, pepi])
    food = Category('Food', 'Put it in your mouth and enjoy', [sausage, parmegiano])
    phones = Category('Phones', 'Pocket devices', [iphone_11, redmi_note_11])
