from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import *


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
    form = TaskForm()
    context_object_name = 'todo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add in a QuerySet of all the books

        context['tasks'] = Task.objects.filter(
            todo_list=Todo.objects.get(pk=self.object.pk))
        context['form'] = self.form

        return context

    def post(self, request, **kwargs):
        self.object = self.get_object()
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.request.path_info)

        return render(request, self.template_name, context=self.get_context_data(**kwargs))

# search works as a "buffer" for when we are obtaining data
# def search(request):
#     if request.method == 'GET':
#         search = request.GET.get('make_task')
        
#         print("ok")
#         return redirect('todo:course', pk=search)