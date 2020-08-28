from django.urls import path
from .views import *

app_name="todolist"

urlpatterns = [
    path('', ListTodos.as_view(), name='index'),
    # path('<int:pk>', ListTodos.as_view(), name='delete'),
    # path('', index, name='index'),
    # path('delete/<int:todo_pk>', delete, name='delete')
]
