from django.shortcuts import render
from django.views import generic

from .models import Todo

def login_page(request):
    return render(request, 'todo/login_page.html')

class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/todo_page.html'
