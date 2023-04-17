from django.contrib import admin
from clients.models import *


# Register your models here.
@admin.register(Clients)
class MyModelAdmin(admin.ModelAdmin):
    ordering = ['name']
