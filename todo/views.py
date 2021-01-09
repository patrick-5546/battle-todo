from django.shortcuts import render
from django.views import generic

from .models import Todo

def login_page(request):
    template = 'login_page.html'

    return render(request, template)

def todo_page(request):
    template = 'todo_page.html'

    return render(request, template)

class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo_page.html'
