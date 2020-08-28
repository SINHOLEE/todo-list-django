# Create your views here.
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import Todo
from .forms import TodoCreateForm
from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404,redirect

from django.db import connection  # for db sql

class ListTodos(APIView):
    
    def get(self, request):
        todos = Todo.objects.all()
        data = request.data
        print(data)
        print(request.query_params)
        print(connection.queries)
        form = TodoCreateForm()
        # return re(todos)
        context = {
            'todo_list':todos, 
            'form':form,
            }
        return render(request, 'todolist/index.html',context=context)
    
    def post(self, request):
        data = request.data
        # save
    
        if data.get('content') is not None and data.get('content') != "":
            content = data.get('content')
            todo = Todo()
            todo.content = content
            todo.save()        
        # delete
        # if data.get('pk') is not None and data.get('pk') != "":
        #     todo = get_object_or_404(Todo, pk=data.get('pk'))
        #     todo.delete()
        # print(connection.queries)
        return redirect('todolist:index')

    def delete(self, request):
        print("11111111111111111111111")
        data = request.data
        print(data)
        if data.get('pk') is not None and data.get('pk') != "":
            todo = get_object_or_404(Todo, pk=int(data.get('pk')))
            todo.delete()
        print(connection.queries)
        return redirect('todolist:index')

# def index(request):
#     todo_list = None
#     if request.method == 'POST':
#         temp = request.POST['content']
#         if temp != '':            
#             todo = Todo()
#             todo.content = temp
#             todo.save()
#     todo_list = Todo.objects.all()
#     return render(request, 'todolist/index.html', {'todo_list':todo_list})


# def delete(request, todo_pk):
#     if request.method == 'POST':
#         delete_todo = get_object_or_404(Todo, pk=todo_pk)
#         delete_todo.delete()
    
#     return redirect('todolist:index')