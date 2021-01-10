from django.shortcuts import render
from django.views import generic

from .models import Todo, Task

def login_page(request):
    template = 'login_page.html'

    return render(request, template)

class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tasks'] = Task.objects.filter(player_team=Team.objects.get(pk=self))
        return context