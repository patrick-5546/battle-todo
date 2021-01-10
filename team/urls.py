from django.urls import path

from . import views

app_name = 'team'  # setting application namespace

urlpatterns = [
    path('<int:pk>/team-hub', views.DetailView.as_view(), name='team-hub'),
    path('<int:pk>/find/', views.find, name='find'),
]
