from rest_framework.serializers import ModelSerializer
from .models import Todo, Priority

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['pk',
        'content',
        'created' ,
        'updated',
        'is_completed' ,
        'priority',
    ]

class PrioritySerializer(ModelSerializer):
    class Meta:
        model = Priority
        fields = ['pk', 'p_type',]