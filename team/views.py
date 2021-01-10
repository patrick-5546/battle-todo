from .models import Team, Player
from django.shortcuts import render
from django.views import generic

# Create your views here.


def teamHub(request):
    return render(request, 'team/team-hub.html')


class DetailView(generic.DetailView):
    model = Team
    template_name = 'team/team-hub.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['team_players'] = Player.objects.filter(
            player_team=Team.objects.get(pk=self.object.pk))
        return context
