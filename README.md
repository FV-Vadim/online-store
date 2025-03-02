# Online_Store

## Разработка интернет магазина

# Описание проекта

Этот проект представляет собой систему управления категориями и продуктами, 
которая позволяет работать с данными о товарах и категориях, хранящимися в JSON-файлах. 
Проект включает в себя функционал для чтения данных из файлов, создания объектов на основе этих данных, 
а также логирования всех операций.

# Чтобы начать работать

Нужно клонировать репозиторий

`git clone https://github.com/FV-Vadim/online-store.git` - клонировать проект на ПК 

Теперь репозиторий успешно склонирован, и вы можете приступать к работе с проектом.

# Основные команды

## Pip

- `pip install package-name` - Установка пакета
- `pip install package-name==4.8.2` - Установка пакета версии 4.8.2
- `python3.13.1 -m pip install package-name` - Установка пакета для Python v3.13.1
- `pip uninstall packege-name` - Удаление пакета
- `python -m pip install --upgrade pip` - Обновление pip
- `pip list` - Вывод списка установленных пакетов
- `pip freeze > requirements.txt` - Запись установленных библиотек в файл
- `pip install -r requirements.txt` - Установка зависимостей сохраненых в проекте

## Poetry

- `poetry init` - Инициализировать пакет в существующем проекте

Активация виртуального окружения:
- `poetry shell` - Активировать виртуальное окружение (Poetry 1.8.5) в Poetry 2.0.0 работает с плагином poetry-plugin-shell
- `poetry env activate` или `.\.venv\Scripts\activate` - Активировать виртуальное окружение (Poetry 2.0.0)
- `pip install poetry-plugin-shell` - Команда для установки плагина poetry-plugin-shell

- `poetry add requests` - Установка библиотек, зависимостей. В пример указан requests.
- `poetry show --tree` - Посмотреть дерево зависимостей
- `poetry add --group dev requests` - Установка группы develop зависимостей. В пример указан requests.

## Poetry add group dev

- `poetry add --group dev mypy` - Установка Mypy
- `poetry add --group dev pytest` - Установка Pytest
- `poetry add --group dev pytest-cov` - Установка Pytest-cov
- `poetry run pytest --cov` - Запуск тестов с оценкой покрытия
- `pytest --cov=src --cov-report=html` - Генерация отчета по покрытию в HTML формате

## Poetry add group lint

- `poetry add --group lint black` - Установка Black
- `poetry add --group lint isort` - Установка Isort
- `poetry add --group lint flake8` - Установка Flake8


## .env

- `pip install python-dotenv` - установка библиотеки Dotenv для чтения файла .env


## .gitignore
- `git add -f htmlcov/index.html` - Команда по добавлению собранной информации о покрытии в HTML
## Git

- `git init` - Создать репозиторий
- `git status` - Посмотреть статус репозитория
- `git add 'Название файла'` - Добавить индекс (выбрать файл для коммита)
- `git commit -m 'Краткое описание что, было сделано'` - Файлы из индекса отправить в репозиторий
- `git log` - Список всех выполненных коммитов, отсортированных по дате выполнения
- `git show 'commit_hash`' - Все изменения, сделанные в рамках одного коммита по хешу
- `git branch develop` - Создание новой ветки в репозитории
- `git checkout -b feature/homework_14_1` - Добалвление ветки с директорией в репозитории


## Основные компоненты проекта

### 1. **Класс `Product`**
Класс `Product` представляет собой модель товара и содержит следующие атрибуты:
- `name` — название товара.
- `description` — описание товара.
- `price` — цена товара.
- `quantity` — количество товара на складе.

### 2. **Класс `Category`**
Класс `Category` представляет собой модель категории товаров и содержит следующие атрибуты:
- `name` — название категории.
- `description` — описание категории.
- `products` — список товаров, относящихся к данной категории.
- `category_count` — счетчик количества созданных категорий.
- `product_count` — счетчик общего количества товаров во всех категориях.

### 3. **Функция `open_file`**
Функция `open_file` предназначена для чтения данных из JSON-файла и возвращения их в виде 
Python-объекта (списка словарей). В случае отсутствия файла функция возвращает пустой список и логирует ошибку.

### 4. **Функция `create_objects_from_json`**
Функция `create_objects_from_json` принимает на вход список словарей, содержащих данные о категориях и продуктах,
и создает на их основе объекты классов `Category` и `Product`. Возвращает список объектов `Category`.

### 5. **Логирование**
В проекте используется модуль `logging` для записи логов в файл. Логирование настроено на уровень `DEBUG`, 
что позволяет отслеживать все операции, включая открытие файлов, создание объектов и обработку ошибок.

### 6. **Тестирование**
Проект включает в себя набор тестов, которые проверяют корректность работы функций и классов. 
Тесты охватывают следующие аспекты:
- Корректность чтения данных из JSON-файла.
- Корректность создания объектов `Category` и `Product`.
- Корректность обработки ошибок (например, отсутствие файла).

## Пример использования

1. **Создание объектов вручную:**
```
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
category1 = Category(
"Смартфоны", 
"Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
[product1, product2]
)
```
```
Продукты:
Название: Samsung Galaxy S23 Ultra
Описание: 256GB, Серый цвет, 200MP камера
Цена: 180000.0
Количество: 5

Название: Iphone 15
Описание: 512GB, Gray space
Цена: 210000.0
Количество: 8

Категории: 
Описание категории: Смартфоны, как средство не только коммуникации, 
но и получения дополнительных функций для удобства жизни
Количество наименований продуктов: 3
Количество категорий: 1
Количество продуктов: 27
```


2. **Чтение данных из JSON-файла и создание объектов:**
```
json_file = "./data/products.json"
data = open_file(json_file)
categories = create_objects_from_json(data)
for category in categories:
   print(f"Категория: {category.name}")
   print(f"Описание: {category.description}")
```
```
Категория: Смартфоны
Описание: Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни  
Категория: Телевизоры
Описание: Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником
```
3. **Логирование:**
   Все операции, такие как открытие файлов, создание объектов и обработка ошибок, логируются в файл `logs/utils.log`.

## Запуск проекта

Для запуска проекта необходимо:
1. Убедиться, что установлен Python 3.x.
2. Установить необходимые зависимости (если есть).
3. Запустить скрипт `main.py`:
   ```bash
   python main.py
   ```




# Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. ниже.

MIT License
Copyright (c) 2025 Vadim Falaleev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.