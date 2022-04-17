from django.contrib import admin
from .models import *

admin.site.register(Order)


@admin.register(OrderOsteopat)
class OrderOsteopatAdmin(admin.ModelAdmin):
    list_display = ('for_', 'status',)

    @admin.display(description='Заявка для')
    def for_(self, obj):
        return f'Заявка для номера: {obj.phone}'

@admin.register(OrderDay)
class OrderDayAdmin(admin.ModelAdmin):
    pass
