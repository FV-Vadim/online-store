import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product1():
    return Product("Iphone 13", "128GB, Зеленый цвет, 128MP камера", 90000.0, 3)


@pytest.fixture
def product2():
    return Product("Samsung Galaxy A53", "256GB, Фиолетовый, 168MP камера", 23000.0, 10)


@pytest.fixture
def product3():
    return Product(
        "Honor", "512GB, Серый цвет, камера с режимом скрытия 128MP", 50000.0, 15
    )


@pytest.fixture
def product4():
    return Product("Macbook Air", "265GB, Черный цвет, 128MP камера", 100000.0, 3)


@pytest.fixture
def category1(product1, product2):
    return Category(
        "Смартфоны",
        "Смартфоны, средство коммуникации, другие функции",
        [product1, product2],
    )


@pytest.fixture
def category2(product3, product4):
    return Category(
        "Ноутбуки",
        "Ноутбуки, это средство для облегчения обучения людей",
        [product3, product4],
    )
