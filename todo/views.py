from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from .models import Todo, Task


def login_page(request):
    template = 'todo/login_page.html'

    return render(request, template)

def registerPage(request):
    form = UserCreationForm()
    template = 'todo/register_page.html'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, template, context)


class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/todo_page.html'
    context_object_name = 'todo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(
            todo_list=Todo.objects.get(pk=self.object.pk))
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