from django.urls import path
from .views import *

app_name = "order"

urlpatterns = [
    path('list/', order_list, name="order_list"),
    path('read/<int:pk>', order_read, name="order_read"),
    path('create/', order_create, name="order_create"),
    path('update/<int:pk>', order_update, name="order_update"),
    path('delete/<int:pk>', order_delete, name="order_delete"),
]
