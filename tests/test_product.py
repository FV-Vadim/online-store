def test_product1(product1):
    assert product1.name == "Iphone 13"
    assert product1.description == "128GB, Зеленый цвет, 128MP камера"
    assert product1.price == 90000.0
    assert product1.quantity == 3


def test_product2(product2):
    assert product2.name == "Samsung Galaxy A53"
    assert product2.description == "256GB, Фиолетовый, 168MP камера"
    assert product2.price == 23000.0
    assert product2.quantity == 10
