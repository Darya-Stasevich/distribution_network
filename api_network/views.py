from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions

from api_network.serializers import ElementsSerializer, ProductSerializer, ElementUpdateSerializer, \
    ElementCreateSerializer, ProductUpdateSerializer

from main.models import Element, Product


class IsActive(permissions.BasePermission):
    """Права доступа к API только активных пользователей"""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active)


class ElementsListView(generics.ListAPIView):
    """API для вывода всех объектов сети"""
    queryset = Element.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = [IsActive]


class ElementsByCountryListView(generics.ListAPIView):
    """API для фильтрации всех объектов сети по стране"""
    queryset = Element.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = [IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contact__address__city']


class ElementsByProductListView(generics.ListAPIView):
    """API для фильтрации всех объектов сети по id продукта"""
    queryset = Element.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = [IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products__id']


class ElementsByDebtListView(generics.ListAPIView):
    """API для объектов сети, задолженность которых превышает среднюю задолженность всех объектов"""
    avg = Element.objects.aggregate(Avg('debt'))
    queryset = Element.objects.filter(debt__gt=avg['debt__avg'])
    serializer_class = ElementsSerializer
    permission_classes = [IsActive]


class ProductCreateView(generics.CreateAPIView):
    """API для создания продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]


class ElementCreateView(generics.CreateAPIView):
    """API для создания объекта сети"""
    queryset = Element.objects.all()
    serializer_class = ElementCreateSerializer
    permission_classes = [IsActive]


class ProductDestroyView(generics.DestroyAPIView):
    """API для удаления продукта по id продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]


class ElementDestroyView(generics.DestroyAPIView):
    """API для удаления объекта сети по id"""
    queryset = Element.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = [IsActive]


class ProductUpdateView(generics.UpdateAPIView):
    """API для обновления продукта по id продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsActive]


class ElementUpdateView(generics.UpdateAPIView):
    """API для обновления объекта сети по id"""
    queryset = Element.objects.all()
    serializer_class = ElementUpdateSerializer
    permission_classes = [IsActive]