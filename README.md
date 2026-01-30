# Final_project

## Шаблон для автоматизации тестирования на python

### Стек:
- pytest
- selenium
- requests
- dotenv
- allure
- config

## Шаблон для автоматизации тестирования на python

### Шаги
1. Склонировать проект 'git clone https://github.com/Heraldica-f/Final_project.git'
2. Установить все зависимости
3. Создать файл '.env' в папке tests
4. Указать в файле '.env' переменную: Kinopoisk_token, где значение Kinopoisk_token - это токен/ключ полученный через Telegram-бот
   Пример:(Переменные вписывать без пробелов до и после '=', а также значение переменных не брать в кавычки)
   Kinopoisk_token=ваш токен/ключ
5. Перейти на [сайт](https://poiskkino.dev/) для получения токена(Ссылка приложена в пункте "Полезные ссылки") и нажать на кнопку "Получить токен", а дальше
4. Запустить все тесты 'python -m pytest tests'
   Запустить отдельно api-тесты 'python -m pytest tests/test_api.py'
   Запустить отдельно ui-тесты 'python -m pytest tests/test_ui.py'

### Библиотеки (!)
- pyp install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install python-dotenv
- pip install allure-pytest

### Струткура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API

### Полезные ссылки
- [Сылка на получение токена](https://poiskkino.dev/)
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)