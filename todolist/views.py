from django.shortcuts import render, HttpResponse
from .models import Todo
from django.shortcuts import get_object_or_404,redirect
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


def delete(request, todo_pk):
    if request.method == 'POST':
        delete_todo = get_object_or_404(Todo, pk=todo_pk)
        delete_todo.delete()
    
    return redirect('todolist:index')