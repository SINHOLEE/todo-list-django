from django_filters.rest_framework import DjangoFilterBackend

from .serializers import TodoSerializer, PrioritySerializer
from .models import Todo, Priority
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import connection  # for db sql
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import APIException, ValidationError
from rest_framework import filters
from pprint import pprint

class TodoModelViewSet(ModelViewSet):
    
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields  = ['=content']

    def get_queryset(self):
        queryset = Todo.objects.all()
        # 완료 여부에 따라 필터링 하는 로직
        is_completed = self.request.query_params.get("is_completed", None)
        if is_completed is not None:
            queryset = queryset.filter(is_completed=int(is_completed))

        # priority에 따라 필터링 하는 로직
        priority = self.request.query_params.get("priority", None)
        if priority is not None:
            queryset = queryset.filter(priority=int(priority))

        # 왜 백그라운드 필터셋이 제대로 작동하지 않을까?

        return queryset

    serializer_class = TodoSerializer

    def get_object(self):
        obj = super().get_object()
        pprint(connection.queries) # 언제 평가가 발생하는지 잘 모르겠다!
        return obj

    # 똑같은거 연속으로 두 번 이상 생성하지 말라는 함수
    def perform_create(self, serializer):
        initial_data = serializer.get_initial()
        content = initial_data.get("content")
        if content is not None:
            todo = Todo.objects.filter(content=content)
            if todo.exists():
                raise ValidationError
            serializer.save()
        pprint(connection.queries)  # 평가 공간



class PriorityModelViewSet(ModelViewSet):

    def get_queryset(self):
        queryset = Priority.objects.all()
        return queryset
    serializer_class = PrioritySerializer

    @action(detail=True)
    def todos(self, request, pk=None):
        queryset = get_object_or_404(Priority, pk=pk)
        serializer = TodoSerializer(queryset.todos.all(), many=True)
        response = Response(serializer.data)
        pprint(connection.queries)  # 평가 공간
        return response

    def get_object(self):
        obj = super().get_object()
        pprint(connection.queries) # 언제 평가가 발생하는지 잘 모르겠다!
        return obj
# class ListTodos(APIView):
    
#     def get(self, request):
#         print("request.method", request.method )
#         todos = Todo.objects.all()
#         data = request.data
#         print(data)
#         print(request.query_params)
#         form = TodoCreateForm()
#         # return re(todos)
#         context = {
#             'todo_list':todos, 
#             'form':form,
#             }
#         print(connection.queries)
#         return render(request, 'todolist/index.html',context=context)
    
#     def post(self, request):
#         print("request.method", request.method )

#         data = request.data
#         # save
    
#         if data.get('content') is not None and data.get('content') != "":
#             content = data.get('content')
#             todo = Todo()
#             todo.content = content
#             todo.save()        
#             print(connection.queries)
#         return redirect('todolist:index')

#     def delete(self, request):
#         print("request.method", request.method )

#         data = request.data
#         if data.get('pk') is not None and data.get('pk') != "":
#             todo = get_object_or_404(Todo, pk=int(data.get('pk')))
#             todo.delete()
#         print(connection.queries)
#         return Response(204)
