from django.contrib import admin
from .models import Data
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('name','age','sex','prediction')

admin.site.register(Data,DataAdmin)