from django.urls import path

from . import views

app_name = 'match'  # setting application namespace

# Using generic views instead of comment block above
# DetailView expects primary key value to be called pk
urlpatterns = [
    # Example useage
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('startgame/', views.startgame, name="startgame"),
    path('results/', views.results, name="results"),
]