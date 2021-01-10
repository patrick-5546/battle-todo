from django.shortcuts import render, redirect
from .game import run
from team.models import Team, Player
from django.urls import reverse

# Create your views here.

def startgame(request):
    return render(request, 'match/startgame.html')

def results(request):
    team1damage = 0
    team2damage = 0

    winner = run(1, 2)
    
    team1 = Team.objects.get(pk = 1)
    team2 = Team.objects.get(pk = 2)
    
    player1 = Player.objects.get(pk = 1)
    player2 = Player.objects.get(pk = 2)
    player3 = Player.objects.get(pk = 3)
    player4 = Player.objects.get(pk = 4)
    player5 = Player.objects.get(pk = 5)
    player6 = Player.objects.get(pk = 6)
    player7 = Player.objects.get(pk = 7)
    player8 = Player.objects.get(pk = 8)
    player9 = Player.objects.get(pk = 9)
    player10 = Player.objects.get(pk = 10)
    
    team1list = [player1, player2, player3, player4, player5]
    team2list = [player6, player7, player8, player9, player10]
    
    for i in range(5):
        team1damage += team1list[i].damage_dealt
        team2damage += team2list[i].damage_dealt

    team1damage = round(team1damage, 2)
    team2damage = round(team2damage, 2)

    team1hp = round(500.0 - team2damage, 2)
    if team1hp <= 0.0: 
        team1hp = 0.0

    team2hp = round(500.0 - team1damage, 2)
    if team2hp <= 0.0:
        team2hp = 0.0

    return render(request, 'match/results.html', {'team1': team1, 'team2': team2, 'team1list': team1list, 'team2list': team2list, 'winner': winner, 'team1damage': team1damage, 'team2damage': team2damage, 'team1hp': team1hp, 'team2hp': team2hp})