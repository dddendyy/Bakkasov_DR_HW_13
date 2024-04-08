import pytest

from classes.product import Product
from classes.category import Category
from classes.smartphone import Smartphone


@pytest.fixture
def zero_product():
    return Product('Zero', 'test exceptions', 100, 0)


@pytest.fixture()
def zero_category():
    return Category('Zero', 'For test', [])


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


@pytest.fixture()
def category_phones():
    return Category('Phones', 'Pocket devices', [Smartphone('Apple', 'Device with bited apple', 160_000, 10, 2.65, 'iPhone 11', 256, 'Black')])


@pytest.fixture()
def smartphone_iphone():
    return Smartphone('Apple', 'Device with bited apple', 160_000, 10, 2.65, 'iPhone 11', 256, 'Black')


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


def test_category_phones_init(category_phones):
    assert category_phones.name == 'Phones'
    assert category_phones.desc == 'Pocket devices'
    assert category_phones.goods_count == 3
    assert category_phones.categories_count == 2
    assert category_phones.goods == 'Apple, 160000.0 руб. Остаток: 10\n'


def test_smartphone_init(smartphone_iphone):
    assert smartphone_iphone.name == 'Apple'
    assert smartphone_iphone.desc == 'Device with bited apple'
    assert smartphone_iphone.price == 160_000.0
    assert smartphone_iphone.available == 10
    assert smartphone_iphone.perfomance == 2.65
    assert smartphone_iphone.model == 'iPhone 11'
    assert smartphone_iphone.memory == 256
    assert smartphone_iphone.color == 'Black'


def test_category_print(category_drink):
    assert category_drink.__str__() == 'Drinks, количество продуктов: 2 шт.'


def test_product_repr(product_sprite):
    assert product_sprite.__repr__() == "Product['Sprite', 'carbonated soft drink with lime and lemon flavor', 75, 25]"


def test_smartphone_repr(smartphone_iphone):
    assert smartphone_iphone.__repr__() == "Smartphone['Apple', 'Device with bited apple', 160000, 10, 2.65, 'iPhone 11', 256, 'Black']"


def test_product_print(product_sprite):
    assert product_sprite.__str__() == 'Sprite, 75 руб. Остаток: 25.'


def test_product_add(product_sprite, product_sausage, smartphone_iphone):
    assert product_sprite + product_sausage == 20_005
    with pytest.raises(TypeError):
        assert product_sprite + smartphone_iphone


def test_product_value_error(product_sausage, zero_product):
    with pytest.raises(ValueError, match='Нельзя складывать товары с нулевым количеством!'):
        assert zero_product + product_sausage
    with pytest.raises(ValueError, match='Нельзя складывать товары с нулевым количеством!'):
        assert product_sausage + zero_product


def test_category_average_error(category_drink, zero_category):
    assert category_drink.average() == 87.0
    assert zero_category.average() == 0


def test_category_value_error(category_drink, zero_product):
    with pytest.raises(ValueError, match='Количество добавляемого товара не может быть нулевым!'):
        assert category_drink.add_goods(zero_product)
