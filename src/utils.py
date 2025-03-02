import json
import os
from typing import Any

from src.category import Category
from src.my_logging import get_logger
from src.product import Product

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "utils.log")
logger = get_logger("utils", file_path)


def open_file(filename: str = "") -> Any:
    """
    Функция открывает JSON-файл и возвращает его содержимое в виде Python-объекта
    :param filename:
    :return:
    """

    try:
        logger.info(
            "Открываем исходный JSON-файл и возвращаем Python объект список словарей."
        )
        data = json.load(
            open(filename, mode="r", encoding="utf-8")
        )  # Открытие файла с кодировкой UTF-8

    except FileNotFoundError:  # Исключение если файл не найден
        logger.error("Файл не найден.")
        return []  # Возвращает пустой список
    else:
        logger.info("Исходный файл успешно преобразован")
        return data


def create_objects_from_json(data):
    """
    Функция принимает на вход список словарей
    :param data: Список словарей с данными о категориях и продуктах
    :return: Список объектов Category
    """

    logger.info("Обработка данных словаря получаемого из JSON-файла")

    category_list = []
    for category in data:
        products_list = []
        for product in category["products"]:
            products_list.append(Product(**product))  # Создаем объекты Product
        category["products"] = products_list
        category_list.append(Category(**category))  # Создаем объекты Category
    return category_list
