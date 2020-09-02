
from rest_framework import routers
from todolist.views import TodoModelViewSet, PriorityModelViewSet
from django.urls import path, include
from rest_framework.routers import url 

routers = routers.SimpleRouter()
routers.register(r'todos', TodoModelViewSet, basename='todos')
routers.register(r'priorites', PriorityModelViewSet, basename='priorities')

urlpatterns = [
    url(r'', include(routers.urls)),
] 
