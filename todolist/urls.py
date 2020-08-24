from django.urls import path
from .views import *

app_name="todolist"

urlpatterns = [
    path('', index, name='index')
]
