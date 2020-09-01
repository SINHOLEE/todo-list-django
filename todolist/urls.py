from rest_framework import routers
from .views import *

routers = routers.SimpleRouter()
routers.register(r'Todos', TodoModelViewSet)

urlpatterns = routers.urls
