def test_category1(category1):
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, средство коммуникации, другие функции"
    assert len(category1.products) == 2

    assert category1.products[0].name == "Iphone 13"
    assert category1.products[0].description == "128GB, Зеленый цвет, 128MP камера"
    assert category1.products[0].price == 90000.0
    assert category1.products[0].quantity == 3

    assert category1.products[1].name == "Samsung Galaxy A53"
    assert category1.products[1].description == "256GB, Фиолетовый, 168MP камера"
    assert category1.products[1].price == 23000.0
    assert category1.products[1].quantity == 10

    assert category1.category_count == 1
    assert category1.product_count == 13


def test_category2(category2):
    assert category2.name == "Ноутбуки"
    assert (
        category2.description == "Ноутбуки, это средство для облегчения обучения людей"
    )
    assert len(category2.products) == 2

    assert category2.products[0].name == "Honor"
    assert (
        category2.products[0].description
        == "512GB, Серый цвет, камера с режимом скрытия 128MP"
    )
    assert category2.products[0].price == 50000.0
    assert category2.products[0].quantity == 15

    assert category2.products[1].name == "Macbook Air"
    assert category2.products[1].description == "265GB, Черный цвет, 128MP камера"
    assert category2.products[1].price == 100000.0
    assert category2.products[1].quantity == 3

    assert category2.category_count == 2
    assert category2.product_count == 31
