Стасевич Дарья Викторовна, Python Developer

Запуск проекта для линукс:
1. Клонируем проект git clone https://github.com/Darya-Stasevich/distribution_network.git
2. Запускам сервер: python3 manage.py runserver
3. Запускаем redis : redis-server
4. Запускаем celery и celery-beat: celery -A  distribution_network worker --beat -l info

Примечания:
Логин и пароль к БД: admin, admin.
Пароль от электронной почты в setting.py - EMAIL_HOST_PASSWORD = 'jbwroevexpzcvmwk' (не знаю, как будет осуществляться проверка выполнения этого пункта задания, если же нужна моя тестовая почта, то нужно прописать EMAIL_HOST_PASSWORD = 'jbwroevexpzcvmwk' в setting.py, иначе с гитхаба меня заспанят)

ЧАСТЬ №1
Все пункты выполнены.

Эндпоинты для пункта 4:
1. http://127.0.0.1:8000/api/all_elements
2. http://127.0.0.1:8000/api/search_by_country (для проверки, например, Беларусь)
3. http://127.0.0.1:8000/api/debt_gt_average
4. http://127.0.0.1:8000/api/search_by_product_id (для проверки, например, 1)
5.
http://127.0.0.1:8000/api/create_element   создание объекта сети (для проверки можно использовать данные ниже)

{
    "category": "ип",
    "title": "Веселый Иван",
    "contact": {
        "email": "ggm@gmail.com",
        "address": {
            "country": "Беларусь",
            "city": "Минск",
            "street": "Розовая",
            "house_number": "19"
        }
    },
    "products": [
        {   "id": 1,
            "title": "Микроволновка",
            "price": "300.00",
            "issue_date": "2022-11-10"
        },
        {
            "title": "Робот-пылесос",
            "price": "600.00",
            "issue_date": "2022-02-01"
        }
    ],
    "workers": [
        {
            "title": "Серый Алексей Юрьевич"
        }
    ],
    "supplier": 1,
    "debt": "800.00"
}

http://127.0.0.1:8000/api/create_product  создание продукта (для проверки можно использовать данные ниже)
{
    "title": "Фен 10",
    "price": "600.00",
    "issue_date": "2022-02-01"
}

http://127.0.0.1:8000/api/delete_element/1  удаление объекта сети  по id (для проверки, например, удаление продукита с id=1)
http://127.0.0.1:8000/api/delete_product/1  удаление продукта по id (для проверки, например, удаление продукта с id=1)

6.
http://127.0.0.1:8000/api/update_element/1  обновление данных объекта сети (для проверки, например, обновление объекта сети с id=1)
http://127.0.0.1:8000/api/update_product/1  обновление продукта по id (для проверки, например, обновление продукта с id=1)



ЧАСТЬ №2
Выполнены все пункты кроме 5(не совсем поняла, что за ключ, если это токен, то проблем его прописать для меня не составляет)
