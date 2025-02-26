
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('register/', Register.as_view(), name='register'),
    path('list/', Register.as_view(), name='list'),
    path('statistics/', Register.as_view(), name='statistics'),

]