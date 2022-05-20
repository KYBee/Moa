from django.urls import path
from .views import *

app_name = "user"

urlpatterns = [
    path('login', user_login, name='user_login'),
    path('logout', user_logout, name='user_logout'),
    path('signup', user_signup, name='user_signup'),
    #path('signup/success/', user_signup_success, name='user_signup_success'),

]
