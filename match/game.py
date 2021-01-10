import random
from .models import Team, Player
   
team1attacking = True
team1PhysDefense = 0
team1SpecDefense = 0
team2PhysDefense = 0
team2SpecDefense = 0
team1HP = 10.0
team2HP = 10.0
baseDamage = 0.5


def playgame(team1, team2):
    global team1PhysDefense
    global team1SpecDefense
    global team2PhysDefense
    global team2SpecDefense

    for player in team1:
        team1PhysDefense += player.physical_defense
        team1SpecDefense += player.special_defense
    
    for player in team2:
        team2PhysDefense += player.physical_defense
        team2SpecDefense += player.special_defense

    for i in range(10):
        currentattacker = determineattacker(team1, team2)
        attack(currentattacker, team1attacking)
        if checkwin(team1attacking):
            return

def determineattacker(team1, team2):
    currentattacker = team1.player1
    global team1attacking
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
        if currentattacker.player_special_select == True:
            currentattacker.damage_dealt += currentattacker.physical_attack/team2PhysDefense + baseDamage
            team2HP -= currentattacker.damage_dealt
        # chose special attack
        else:
            currentattacker.damage_dealt += currentattacker.physical_attack/team2SpecDefense + baseDamage
            team2HP -= currentattacker.damage_dealt
    
    # player from team 2 attacks team 1
    else:
        # chose physical attack
        if currentattacker.player_special_select == True:
            currentattacker.damage_dealt += currentattacker.physical_attack/team1PhysDefense + baseDamage
            team1HP -= currentattacker.damage_dealt
        # chose special attack
        else:
            currentattacker.damage_dealt += currentattacker.physical_attack/team1SpecDefense + baseDamage
            team1HP -= currentattacker.damage_dealt
    currentattacker.has_attacked = True
        
def checkwin(team1attacking):
    global team1HP
    global team2HP
    # check if team 1 won
    if team1attacking == True:
        if team2HP <= 0.0:
            team2HP = 0.0
            return True
        else:
            return False
    # check if team 2 won
    else:
        if team1HP <= 0.0:
            team1HP = 0.0
            return True
        else:
            return False



        