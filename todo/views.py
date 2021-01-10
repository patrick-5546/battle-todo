from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import generic

from .models import Todo, Task
from .forms import TaskForm


def login_page(request):
    template = 'todo/login_page.html'

    return render(request, template)


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
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(task_name=form.cleaned_data.get('task_name'),
                        task_description=form.cleaned_data.get('task_description'),
                        todo_list=Todo.objects.get(pk=pk))
            task.save()
            return redirect('todo:todo', pk=pk)

    print('failed attempt')
    return redirect('todo:todo', pk=pk)