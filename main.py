from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json, open_file

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(f"Название: {product1.name}")
    print(f"Описание: {product1.description}")
    print(f"Цена: {product1.price}")
    print(f"Количество: {product1.quantity}\n")

    print(f"Название: {product2.name}")
    print(f"Описание: {product2.description}")
    print(f"Цена: {product2.price}")
    print(f"Количество: {product2.quantity}\n")

    print(f"Название: {product3.name}")
    print(f"Описание: {product3.description}")
    print(f"Цена: {product3.price}")
    print(f"Количество: {product3.quantity}\n")

    category1 = Category(
        "Смартфоны\n",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(f'Проверка совпадения названия категории: {category1.name == "Смартфоны"}\n')
    print(f"Описание категории: {category1.description}")
    print(f"Количество наименований продуктов: {len(category1.products)}")
    print(f"Количество категорий: {category1.category_count}")
    print(f"Количество продуктов: {category1.product_count}\n")

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(f"Название категории: {category2.name}")
    print(f"Описание категории: {category2.description}")
    print(f"Количество наименований продуктов: {len(category2.products)}")
    print(f"Количество продуктов: {category2.products}\n")

    print(f"Количество категорий: {Category.category_count}")
    print(f"Количество продуктов: {Category.product_count}")

    json_file = "./data/products.json"
    print(f"Продукция на складе:\n {open_file(json_file)}")

    users_data = create_objects_from_json(open_file(json_file))
    for category in users_data:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
