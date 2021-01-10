from .models import Team, Player
from django.shortcuts import render, redirect
from django.views import generic

from .models import Team, Player


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
            player_team=Team.objects.get(pk=self.object.pk))[:5]
        context['player_leaderboards'] = Player.objects.order_by('-player_points')[:10]
        context['team_leaderboards'] = Team.objects.order_by('-team_points')[:10]
        return context

def find(request, pk):
    if request.method == 'POST':
        player = Player.objects.get(pk=pk)
        todo_points = player.todo_points
        cool = request.POST.get('select')
        player_special_select = True if cool == 'special' else False

        physical_attack = int(request.POST.get(
            'physical_attack')) - player.physical_attack
        physical_defense = int(request.POST.get(
            'physical_defense')) - player.physical_defense
        special_attack = int(request.POST.get(
            'special_attack')) - player.special_attack
        special_defense = int(request.POST.get(
            'special_defense')) - player.special_defense
        speed = int(request.POST.get('speed')) - player.speed

        sum_dif = physical_attack + physical_defense + \
        special_attack + special_defense + speed

        if sum_dif <= todo_points:
            player.physical_attack += physical_attack
            player.physical_defense += physical_defense
            player.special_attack += special_attack
            player.special_defense += special_defense
            player.speed += speed
            player.todo_points -= sum_dif
            player.player_special_select = player_special_select
            player.save()

    else:
        print('failed attempt')

    return redirect('team:team-hub', pk=player.player_team.pk)
