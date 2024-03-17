import pytest

from scripts.main import Product, Category

@pytest.fixture()
def product_sprite():
    return Product('Sprite', 'carbonated soft drink with lime and lemon flavor', 75, 25)


@pytest.fixture()
def category_drink():
    return Category('Drinks', 'just drink it', ['Sprite', 'Pepi'])


def test_product_init(product_sprite):
    assert product_sprite.name == 'Sprite'
    assert product_sprite.desc == 'carbonated soft drink with lime and lemon flavor'
    assert product_sprite.price == 75.0
    assert product_sprite.available == 25


def test_category_init(category_drink):
    assert category_drink.name == 'Drinks'
    assert category_drink.desc == 'just drink it'
    assert category_drink.goods == ['Sprite', 'Pepi']
    assert category_drink.goods_count == 2
    assert category_drink.categories_count == 3 # в main уже инициализированны 2 экземпляра