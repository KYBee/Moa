from django.urls import path
from . import views

app_name = "funding"

urlpatterns = [
    # User 펀딩 목록 조회 : pk -> user.pk
    path('read/<int:pk>/', funding_read, name = 'funding_read'),
    # 펀딩 개설
    path('create/', funding_create, name = 'funding_create'),
    # 펀딩 취소 : pk -> funding.pk
    path('delete/<int:pk>', funding_delete, name = 'funding_delete'),
]
