from django.shortcuts import render
from django.views import generic

from .models import Todo, Task

def login_page(request):
    template = 'todo/login_page.html'

    return render(request, template)

def todo_page(request):
    template = 'todo/todo_page.html'

    return render(request, template)

class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/todo_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tasks'] = Task.objects.filter(
            todo_list=Todo.objects.get(pk=self.object.pk))
        return context
