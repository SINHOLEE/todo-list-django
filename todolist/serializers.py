from rest_framework.serializers import ModelSerializer, StringRelatedField, HyperlinkedRelatedField, ManyRelatedField
from .models import Todo, Priority
from rest_framework.utils.serializer_helpers import BindingDict


class DynamicFieldsModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')

        # print("@@@@@@@@@@@@@@")
        # print("@@@@@@@@@@@@@@")
        # print("@@@@@@@@@@@@@@")
        print("@@@@@@@@@@@@@@")
        print(self)
        print(kwargs)
        print("args: ", args)
        print("@@@@@@@@@@@@@@")
        # print("@@@@@@@@@@@@@@")
        # print("@@@@@@@@@@@@@@")
        # print("@@@@@@@@@@@@@@")
        if request:
            fields = request.query_params.get('fields')
            # print(fields)
            if fields:
                fields = fields.split(',')
                # Drop any fields that are not specified in the `fields` argument.
                allowed = set(fields)
                existing = set(self.fields.keys())
                # print(allowed)
                # print(existing)
                # print(type(self.fields))
                for field_name in existing - allowed:
                
                    print("poped field_name: %s, %s" % (field_name , self.fields.pop(field_name)))


class TodoSerializer(DynamicFieldsModelSerializer, ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ['pk', 'content', 'created','updated', 'is_completed',]
        # fields = '__all__' # 이렇게 하면, 관계형으로 표현할 때, pk와 id가 혼용되어 나타난다.

    
        
class PrioritySerializer(DynamicFieldsModelSerializer, ModelSerializer):

    class Meta:
        model = Priority
        fields = ['id', 'p_type']


class DetailedTodoSerializer(DynamicFieldsModelSerializer, ModelSerializer):
    priority = PrioritySerializer(many=False)

    class Meta:
        model = Todo
        fields = ['pk', 'content', 'created','updated', 'is_completed', 'priority']
        # fields = '__all__' # 이렇게 하면, 관계형으로 표현할 때, pk와 id가 혼용되어 나타난다.

        
class DetaildPrioritySerializer(DynamicFieldsModelSerializer, ModelSerializer):
    # from .serializers import TodoSerializer
    todos = TodoSerializer(
        many=True

    )
    class Meta:
        model = Priority
        fields = ['id', 'p_type','todos',]