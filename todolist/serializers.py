from rest_framework.serializers import ModelSerializer
from .models import Todo

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['content',
    'created' ,
    'updated',
    'is_completed' ,
    ]