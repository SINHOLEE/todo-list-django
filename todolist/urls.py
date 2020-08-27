from django.urls import path
from .views import *

app_name="todolist"

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:todo_pk>', delete, name='delete')
]
