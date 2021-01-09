from django.urls import path

from . import views

app_name = 'todo'  # setting application namespace

# Using generic views instead of comment block above
# DetailView expects primary key value to be called pk
urlpatterns = [
    path('', views.login_page, name='login'),
    path('<int:pk>/todo', views.DetailView.as_view(), name='todo'),
]