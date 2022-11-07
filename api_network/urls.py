from django.urls import path

from api_network.views import ElementsByCountryListView, ElementsListView, ElementsByProductListView, \
    ElementsByDebtListView, ProductCreateView, ProductDestroyView, ElementCreateView, ElementDestroyView, \
    ProductUpdateView, ElementUpdateView, ElemQrCreateView

app_name = 'api_network'

urlpatterns = [
    path('all_elements', ElementsListView.as_view()),
    path('search_by_country', ElementsByCountryListView.as_view()),
    path('search_by_product_id', ElementsByProductListView.as_view()),
    path('debt_gt_average', ElementsByDebtListView.as_view()),
    path('create_product', ProductCreateView.as_view()),
    path('create_element', ElementCreateView.as_view()),
    path('delete_product/<int:pk>', ProductDestroyView.as_view()),
    path('delete_element/<int:pk>', ElementDestroyView.as_view()),
    path('update_product/<int:pk>', ProductUpdateView.as_view()),
    path('update_element/<int:pk>', ElementUpdateView.as_view()),
    path('qr', ElemQrCreateView.as_view()),
]
