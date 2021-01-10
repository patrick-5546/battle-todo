import json

player_fixtures = [
    {
        'model': 'team.player',
        'pk': 1,
        'fields': {
            'player_name': 'a',
            'player_points': 0,
            'player_team': 1,
            'player_special_select': False,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 0,
            'physical_attack': 1,
            'physical_defense': 1,
            'special_attack': 1,
            'special_defense': 1,
            'speed': 1
        }
    }
]

team_fixtures = [
    {
        'model': 'team.team',
        'pk': 1,
        'fields': {
            'team_name': 'team_1',
            'team_points': 0
        }
    }
]

with open('team/fixtures/team/fixtures.json', 'w') as outfile:
    json.dump(team_fixtures + player_fixtures, outfile)