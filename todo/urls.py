from django.urls import path

from . import views

app_name = 'todo'  # setting application namespace

urlpatterns = [
    path('', views.login_page, name='login'),
    path('<int:pk>/todo', views.DetailView.as_view(), name='todo'),
    path('<int:pk>/search/', views.search, name='search'),
]