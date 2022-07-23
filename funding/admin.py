from django.contrib import admin
from .models import *

@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = ['order', 'participant']