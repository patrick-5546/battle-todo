from django.contrib import admin

from .models import Todo, Task

class TaskInline(admin.StackedInline):
    model = Task
    extra = 5

class TodoAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
    search_fields = ['user']

admin.site.register(Todo, TodoAdmin)
