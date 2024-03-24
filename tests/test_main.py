import pytest

from scripts.product import Product
from scripts.category import Category

@pytest.fixture()
def product_sprite():
    return Product('Sprite', 'carbonated soft drink with lime and lemon flavor', 75, 25)

@pytest.fixture()
def product_sausage():
    return Product('Sausage', 'a food product', 259, 70)

@pytest.fixture()
def category_drink():
    return Category('Drinks', 'just drink it', [Product('Sprite', 'carbonated soft drink with lime and lemon flavor', 75, 25),
                                                Product('Pepi', 'carbonated soft drink produced by PepsiCo', 99, 49)])


def test_product_init(product_sprite):
    assert product_sprite.name == 'Sprite'
    assert product_sprite.desc == 'carbonated soft drink with lime and lemon flavor'
    assert product_sprite.price == 75.0
    assert product_sprite.available == 25


def test_category_init(category_drink):
    assert category_drink.name == 'Drinks'
    assert category_drink.desc == 'just drink it'
    assert category_drink.goods_count == 2
    assert category_drink.categories_count == 1
    assert category_drink.goods == 'Sprite, 75.0 руб. Остаток: 25\nPepi, 99.0 руб. Остаток: 49\n'


def test_category_print(category_drink):
    assert category_drink.__str__() == 'Drinks, количество продуктов: 2 шт.'


def test_product_print(product_sprite):
    assert product_sprite.__str__() == 'Sprite, 75 руб. Остаток: 25.'


def test_product_add(product_sprite, product_sausage):
    assert product_sprite + product_sausage == 20_005
