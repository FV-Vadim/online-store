from unittest.mock import mock_open, patch

from src.utils import create_objects_from_json, open_file

data: str = """
[
    {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром",
        "products": [
            {
                "name": "55\\" QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }
        ]
    }
]
"""


# Тест функции get_json_transactions по типу выходного значения
@patch("builtins.open", mock_open(read_data=data))
def test_open_file_list() -> None:
    assert type(open_file()) is list


# Тест функции get_json_transactions на соответствие выходного значения
@patch("builtins.open", mock_open(read_data=data))
def test_open_file() -> None:
    assert open_file()[0]["products"][0]["description"] == "Фоновая подсветка"


def test_open_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        assert (
            open_file("non_existent_file.json") == []
        )  # Проверяем, что функция возвращает []


def test_create_objects_from_json_assert():
    # Тестовые данные
    test_data = [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром",
            "products": [
                {
                    "name": '55" QLED 4K',
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7,
                }
            ],
        }
    ]

    # Вызов функции
    result = create_objects_from_json(test_data)

    # Проверка
    assert result[0].products[0].description == "Фоновая подсветка"
