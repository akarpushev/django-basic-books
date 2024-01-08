from django.db import models


# Список категорий
categories_data = [
    {
        'name': 'Python',
        'slug': 'python',
    },
    {
        'name': 'Веб-разработка',
        'slug': 'web-development',
    },
    {
        'name': 'JavaScript',
        'slug': 'javascript',
    },
]

# Список книг
books = [
    {
        'id': 1,
        'title': 'Flask в действии',
        'description': 'Погружение в веб-разработку с использованием Flask.',
        'author': 'Мигель Гринберг',
        'published_year': 2014,
        'category': 'web-development',
    },
    {
        'id': 2,
        'title': 'Django для начинающих',
        'description': 'Изучение веб-разработки с использованием Django.',
        'author': 'Уильям С. Винсент',
        'published_year': 2018,
        'category': 'web-development',
    },
    {
        'id': 3,
        'title': 'Python. Эффективное программирование',
        'description': 'Освоение эффективных практик программирования на Python.',
        'author': 'Бретт Слэткин',
        'published_year': 2015,
        'category': 'python',
    },
    {
        'id': 4,
        'title': 'Fluent Python',
        'description': 'Продвинутое программирование на Python.',
        'author': 'Люсиано Рамалью',
        'published_year': 2015,
        'category': 'python',
    },
    {
        'id': 5,
        'title': 'JavaScript и jQuery: Новые возможности',
        'description': 'Изучение веб-разработки с использованием JavaScript и jQuery.',
        'author': 'Дэвид Сойер Макфарланд',
        'published_year': 2014,
        'category': 'javascript',
    },
    {
        'id': 6,
        'title': 'Python. Тестирование программ',
        'description': 'Практическое руководство по тестированию программ на Python.',
        'author': 'Брайан Окенхейм',
        'published_year': 2014,
        'category': 'python',
    },
    {
        'id': 7,
        'title': 'Flask Web Development',
        'description': 'Developing Web Applications with Python and Flask.',
        'author': 'Miguel Grinberg',
        'published_year': 2014,
        'category': 'web-development',
    },
    {
        'id': 8,
        'title': 'Python Crash Course',
        'description': 'A Hands-On, Project-Based Introduction to Programming.',
        'author': 'Eric Matthes',
        'published_year': 2015,
        'category': 'python',
    },
    {
        'id': 9,
        'title': 'Vue.js в действии',
        'description': 'Разработка современных веб-приложений с использованием Vue.js.',
        'author': 'Эрик Рэндольф',
        'published_year': 2018,
        'category': 'web-development',
    },
    {
        'id': 10,
        'title': 'Effective Python: 90 способов улучшить свой Python код',
        'description': 'Рекомендации по улучшению стиля и эффективности написания Python кода.',
        'author': 'Бретт Слэткин',
        'published_year': 2015,
        'category': 'python',
    },
]