Стасевич Дарья Викторовна, Python Developer

Запуск проекта для линукс:
1. Клонируем проект git clone https://github.com/Darya-Stasevich/distribution_network.git
2. Запускам сервер: python3 manage.py runserver
3. Запускаем redis : redis-server
4. Запускаем celery и celery-beat: celery -A  distribution_network worker --beat -l info


ЧАСТЬ №1
Все пункты выполнены.

Эндпоинты для пункта 4:
4.1. http://127.0.0.1:8000/api/all_elements
4.2. http://127.0.0.1:8000/api/search_by_country (для проверки, например, Беларусь)
4.3. http://127.0.0.1:8000/api/debt_gt_average
4.4. http://127.0.0.1:8000/api/search_by_product_id (для проверки, например, 1)
4.5.
создание объекта сети
создание продукта
удаление объекта сети
удаление продукта
4.6.
обновление данных объекта сети
обновление продукта

ЧАСТЬ №2
Выполнены все пункты кроме 5.
