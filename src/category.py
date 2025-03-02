class Category:
    name: str  # Название категории
    description: str  # Описание категории
    products: list  # Список Продуктов данной категории
    category_count = 0  # Количество категорий
    product_count = 0  # Количество продуктов

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        for product in products:
            Category.product_count += product.quantity
