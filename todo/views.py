from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import generic

from .models import Todo, Task
from team.models import Team, Player


def login_page(request):
    template = 'todo/login_page.html'

    return render(request, template)

def registerPage(request):
    template = 'todo/register_page.html'

    return render(request, template)


class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/todo_page.html'
    context_object_name = 'todo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(
            todo_list=Todo.objects.get(pk=self.object.pk))
        context['todopoints'] = 0
        for task in context['tasks']:
            if task.completion_status == True:
                context['todopoints'] += 5
        Todo.player.todo_points = context['todopoints']
        return context

def search(request, pk):
    if request.method == 'POST':
        if 'completion_status' in request.POST:
            task_name = request.POST.get('completion_status').split(': ')[1]
            task = Task.objects.get(task_name=task_name)
            task.completion_status = True
        else:
            task_name = request.POST.get('task_name')
            task_description = request.POST.get('task_description')
            try:
                task = Task.objects.get(task_name=task_name)
                task.task_description = task_description
            except Task.DoesNotExist:
                task = Task(task_name=task_name, task_description=task_description,
                            todo_list=Todo.objects.get(pk=pk))
        task.save()
    else:
        print('failed attempt')
    
    return redirect('todo:todo', pk=pk)