from django.urls import path
from .views import *

app_name = "funding"

urlpatterns = [
    path('list', funding_list, name = 'funding_list'),
    # 펀딩 개설 : pk -> order.pk
    path('create/<int:pk>', funding_create, name = 'funding_create'),
    # 펀딩 취소 : pk -> funding.pk
    path('delete/<int:pk>', funding_delete, name = 'funding_delete'),
]
