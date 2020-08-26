from django.shortcuts import render, HttpResponse
from .models import Todo

# Create your views here.
def index(request):
    todo_list = None
    if request.method == 'POST':
        temp = request.POST['content']
        if temp != '':            
            todo = Todo()
            todo.content = temp
            todo.save()
    todo_list = Todo.objects.all()
    return render(request, 'todolist/index.html', {'todo_list':todo_list})