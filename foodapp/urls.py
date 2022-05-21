from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name=''),
    path('delete/<id>', delete_consume, name='delete'),
]