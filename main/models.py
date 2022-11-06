from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class Element(models.Model):
    """Модель объекта сети"""
    CHAIN = (
        ("завод", "завод"),
        ("дистрибьютер", "дистрибьютер"),
        ("дилер", "дилер"),
        ("розница", "розница"),
        ("ип", "ип"),
    )
    category = models.CharField(max_length=20, choices=CHAIN, verbose_name="Звено сети")
    title = models.CharField(max_length=50, verbose_name='Наименование звена сети')
    contact = models.OneToOneField('Contact', on_delete=models.CASCADE,
                                   verbose_name="Контакты")
    products = models.ManyToManyField('Product', related_name='elements', verbose_name="Продукты", blank=True, null=True)
    supplier = models.ForeignKey('Element', on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="Поставщик")
    debt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0,
                               validators=[MinValueValidator(Decimal('0.00'))], verbose_name="Задолженность")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        ordering = ['created', ]
        verbose_name = "Объект сети"
        verbose_name_plural = "Объекты сети"

    def __str__(self):
        return self.title

    def clean(self):
        if self.supplier:
            if self.category == 'завод':
                if self.supplier.category in ('завод', 'дистрибьютер', 'дилер', 'ип', 'розница'):
                    raise ValidationError("У завода нет поставщика. Не заполняйте данное поле")
            if self.category == 'дистрибьютер':
                if self.supplier.category in ('дистрибьютер', 'дилер', 'ип', 'розница'):
                    raise ValidationError(f"{self.supplier.category} не может быть поставщиком для дистербьютера")
            if self.category == 'дилер':
                if self.supplier.category in ('дилер', 'ип', 'розница'):
                    raise ValidationError(f"{self.supplier.category} не может быть поставщиком для дилера")
            if self.category == 'розница':
                if self.supplier.category in ('ип', 'розница'):
                    raise ValidationError(f"{self.supplier.category} не может быть поставщиком для розницы")
            if self.category == 'ип':
                if self.supplier.category in ('ип',):
                    raise ValidationError(f"{self.supplier.category} не может быть поставщиком для ип")


class Product(models.Model):
    """Модель продукта"""
    title = models.CharField(max_length=25, verbose_name='Наименование товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))],
                                verbose_name='Цена')
    issue_date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title


class Worker(models.Model):
    """Модель сотрудника"""
    title = models.CharField(max_length=70, verbose_name="ФИО сотрудника")
    element = models.ForeignKey('Element', related_name='workers', on_delete=models.CASCADE, verbose_name="Звено")

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.title


class Contact(models.Model):
    """Модель контактов"""
    email = models.EmailField()
    address = models.OneToOneField('Address', on_delete=models.CASCADE, verbose_name="Адрес")

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.email}, {self.address}"


class Address(models.Model):
    """Модель адреса"""
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=50, verbose_name="Улица")
    house_number = models.CharField(max_length=7, verbose_name="Номер дома")

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}, {self.house_number}"
