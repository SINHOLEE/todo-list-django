from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<html><title>Todo List</title></html>')
    # return render(request, 'todolist/index.html')