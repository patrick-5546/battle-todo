import random
from team.models import Team, Player
   
team1attacking = True
team1PhysDefense = 0
team1SpecDefense = 0
team2PhysDefense = 0
team2SpecDefense = 0
team1HP = 500.0
team2HP = 500.0
baseDamage = 50.0

def run(pk1, pk2):
    team1 = Team.objects.get(pk = pk1)
    team2 = Team.objects.get(pk = pk2)
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
    team1.team_points = 0
    team2.team_points = 0
    resetgamestate(team1list, team2list)
    winner = playgame(team1, team2, team1list, team2list)
    player1.save()
    player2.save()
    player3.save()
    player4.save()
    player5.save()
    player6.save()
    player7.save()
    player8.save()
    player9.save()
    player10.save()
    team1.save()
    team2.save()
    return winner

def resetgamestate(team1list, team2list):
    global team1PhysDefense
    global team1SpecDefense
    global team2PhysDefense
    global team2SpecDefense
    global team1HP
    global team2HP

    for i in range(5):
        team1list[i].has_attacked = False
        team2list[i].has_attacked = False
        team1list[i].damage_dealt = 0
        team2list[i].damage_dealt = 0

    team1PhysDefense = 0
    team1SpecDefense = 0
    team2PhysDefense = 0
    team2SpecDefense = 0
    team1HP = 500.0
    team2HP = 500.0

def playgame(team1, team2, team1list, team2list):
    global team1PhysDefense
    global team1SpecDefense
    global team2PhysDefense
    global team2SpecDefense

    for player in team1list:
        team1PhysDefense += player.physical_defense
        team1SpecDefense += player.special_defense
    
    for player in team2list:
        team2PhysDefense += player.physical_defense
        team2SpecDefense += player.special_defense

    for i in range(10):
        currentattacker = determineattacker(team1list, team2list)
        attack(currentattacker, team1attacking)
        if checkwin(team1, team2, team1attacking):
            if team1attacking == True:
                return True
            else: 
                return False
    
    # win condition if no team knocks the other out
    if team1HP > team2HP:
        team1.team_points += 5
        team2.team_points -= 5
        return True
    else:
        team1.team_points -= 5
        team2.team_points += 5
        return False
    
def determineattacker(team1, team2):
    global team1attacking
    currentattacker = Player(speed = 0)

    for player in team1:
        # faster
        if player.speed > currentattacker.speed and player.has_attacked == False: 
            currentattacker = player
            team1attacking = True
        # speed tie; random 50/50 chance
        elif player.speed == currentattacker.speed and player.has_attacked == False and round(random.uniform(0, 1), 0) == 1:
                currentattacker = player
                team1attacking = True

    for player in team2:
        # faster
        if player.speed > currentattacker.speed and player.has_attacked == False:
            currentattacker = player
            team1attacking = False
        # speed tie; random 50/50 chance
        elif player.speed == currentattacker.speed and player.has_attacked == False and round(random.uniform(0, 1), 0) == 1:
                currentattacker = player
                team1attacking = False

    return currentattacker

def attack(currentattacker, team1attacking):
    global team1HP
    global team2HP
    # player from team 1 attacks team 2
    if team1attacking == True:
        # chose physical attack
        if currentattacker.player_special_select == False:
            currentattacker.damage_dealt += round(currentattacker.physical_attack/team2PhysDefense * 100 + baseDamage, 2)
            team2HP -= currentattacker.damage_dealt
        # chose special attack
        else:
            currentattacker.damage_dealt += round(currentattacker.special_attack/team2SpecDefense * 100 + baseDamage, 2)
            team2HP -= currentattacker.damage_dealt
    
    # player from team 2 attacks team 1
    else:
        # chose physical attack
        if currentattacker.player_special_select == False:
            currentattacker.damage_dealt += round(currentattacker.physical_attack/team1PhysDefense * 100 + baseDamage, 2)
            team1HP -= currentattacker.damage_dealt
        # chose special attack
        else:
            currentattacker.damage_dealt += round(currentattacker.special_attack/team1SpecDefense * 100 + baseDamage, 2)
            team1HP -= currentattacker.damage_dealt
    currentattacker.has_attacked = True
        
def checkwin(team1, team2, team1attacking):
    global team1HP
    global team2HP
    # check if team 1 won
    if team1attacking == True:
        if team2HP <= 0.0:
            team2HP = 0.0
            team1.team_points += 10
            team2.team_points -= 10
            return True
        else:
            return False
    # check if team 2 won
    else:
        if team1HP <= 0.0:
            team1HP = 0.0
            team2.team_points += 10
            team1.team_points -= 10
            return True
        else:
            return False



        