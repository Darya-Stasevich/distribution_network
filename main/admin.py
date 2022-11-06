from django.contrib import admin
from django.utils.html import format_html

from main.models import *


@admin.action(description='Очистить задолженность')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class WorkerInline(admin.StackedInline):
    model = Worker


class ElementAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'contact', 'view_supplier', 'debt']
    list_filter = ('contact__address__country',)
    inlines = [WorkerInline, ]
    actions = [clear_debt]
    change_form_template = "admin/model_change_form.html"

    def view_supplier(self, obj):
        if obj.supplier:
            return format_html(
                f'<a href="http://127.0.0.1:8000/admin/main/element/{obj.supplier.id}/change/">{obj.supplier}</a>')

    view_supplier.short_description = 'Ссылка на страницу Поставщика'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'issue_date']


admin.site.register(Element, ElementAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Worker)
admin.site.register(Contact)
admin.site.register(Address)
