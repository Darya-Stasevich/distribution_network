import datetime

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from main.models import Element, Worker, Product, Contact, Address


class ElementsSerializer(serializers.ModelSerializer):
    """Сериализатор объектов сети для отображения всей информации"""
    contact = serializers.StringRelatedField()
    workers = serializers.StringRelatedField(many=True)
    products = serializers.StringRelatedField(many=True)
    supplier = serializers.StringRelatedField()

    class Meta:
        model = Element
        fields = ['id', 'category', 'title', 'contact', 'products', 'workers', 'supplier', 'debt', 'created']


class ProductSerializer(WritableNestedModelSerializer):
    """Сериализатор для продукта"""

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'issue_date']


class WorkerSerializer(WritableNestedModelSerializer):
    """Сериализатор для работника"""

    class Meta:
        model = Worker
        fields = ['id', 'title']


class AddressSerializer(WritableNestedModelSerializer):
    """Сериализатор для адреса"""

    class Meta:
        model = Address
        fields = '__all__'


class ContactSerializer(WritableNestedModelSerializer):
    """Сериализатор для контакта"""

    address = AddressSerializer()

    class Meta:
        model = Contact
        fields = ['id', 'email', 'address']


class ElementCreateSerializer(WritableNestedModelSerializer):
    """Сериализатор объектов сети при его создании"""
    contact = ContactSerializer()
    workers = WorkerSerializer(many=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = Element
        fields = ['id', 'category', 'title', 'contact', 'products', 'workers', 'supplier', 'debt']


def validate_date(date):
    """Функция для валидации поля issue_date в сериализаторе ProductUpdateSerializer"""
    if (date - datetime.date.today()).days > 0:
        raise ValidationError('Дата выхода продукта на рынок не может превышать текущую дату')


class ProductUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для продукта, проверка названия продукта и даты выхода продукта на рынок"""
    title = serializers.CharField(max_length=25)
    issue_date = serializers.DateField(validators=[validate_date])

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'issue_date']


class ElementUpdateSerializer(WritableNestedModelSerializer):
    """Сериализатор обновления обьъекта сети"""
    debt = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=50)
    contact = ContactSerializer()
    workers = WorkerSerializer(many=True)
    products = ProductUpdateSerializer(many=True)

    class Meta:
        model = Element
        fields = ['id', 'category', 'title', 'contact', 'products', 'workers', 'supplier', 'debt']


class ElementQrSerializer(serializers.ModelSerializer):
    """Сериализатор названия объекта сети для генерации qr-кода"""
    class Meta:
        model = Element
        fields = ['title', ]