import json

todo_fixtures = [
    {
        'model': 'todo.todo',
        'pk': 1,
        'fields': {
            'player': 1,
        }
    },
    {
        'model': 'todo.todo',
        'pk': 2,
        'fields': {
            'player': 2,
        }
    }, 
    {
        'model': 'todo.todo',
        'pk': 3,
        'fields': {
            'player': 3,
        }
    },
    {
        'model': 'todo.todo',
        'pk': 4,
        'fields': {
            'player': 4,
        }
    }, 
    {
        'model': 'todo.todo',
        'pk': 5,
        'fields': {
            'player': 5,
        }
    },
    {
        'model': 'todo.todo',
        'pk': 6,
        'fields': {
            'player': 6,
        }
    }, 
    {
        'model': 'todo.todo',
        'pk': 7,
        'fields': {
            'player': 7,
        }
    },
    {
        'model': 'todo.todo',
        'pk': 8,
        'fields': {
            'player': 8,
        }
    }, 
    {
        'model': 'todo.todo',
        'pk': 9,
        'fields': {
            'player': 9,
        }
    },
    {
        'model': 'todo.todo',
        'pk': 10,
        'fields': {
            'player': 10,
        }
    }
]

player_fixtures = [
    {
        'model': 'team.player',
        'pk': 1,
        'fields': {
            'player_name': 'Sharon',
            'player_points': 2,
            'player_team': 1,
            'player_special_select': True,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 0,
            'physical_defense': 0,
            'special_attack': 0,
            'special_defense': 0,
            'speed': 5
        }
    },
    {
        'model': 'team.player',
        'pk': 2,
        'fields': {
            'player_name': 'Olivia',
            'player_points': 14,
            'player_team': 1,
            'player_special_select': False,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 6,
            'physical_defense': 1,
            'special_attack': 1,
            'special_defense': 1,
            'speed': 1
        }
    },
    {
        'model': 'team.player',
        'pk': 3,
        'fields': {
            'player_name': 'Bob',
            'player_points': 81,
            'player_team': 1,
            'player_special_select': True,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 1,
            'physical_defense': 5,
            'special_attack': 2,
            'special_defense': 3,
            'speed': 1
        }
    },
    {
        'model': 'team.player',
        'pk': 4,
        'fields': {
            'player_name': 'Alvin',
            'player_points': 55,
            'player_team': 1,
            'player_special_select': False,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 4,
            'physical_defense': 1,
            'special_attack': 1,
            'special_defense': 1,
            'speed': 6
        }
    },
    {
        'model': 'team.player',
        'pk': 5,
        'fields': {
            'player_name': 'Ryan',
            'player_points': 65,
            'player_team': 1,
            'player_special_select': False,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 5,
            'physical_defense': 6,
            'special_attack': 1,
            'special_defense': 1,
            'speed': 1
        }
    },
    {
        'model': 'team.player',
        'pk': 6,
        'fields': {
            'player_name': 'Chris',
            'player_points': 42,
            'player_team': 2,
            'player_special_select': True,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 1,
            'physical_defense': 1,
            'special_attack': 5,
            'special_defense': 4,
            'speed': 1
        }
    },
    {
        'model': 'team.player',
        'pk': 7,
        'fields': {
            'player_name': 'Joe',
            'player_points': 69,
            'player_team': 2,
            'player_special_select': False,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 4,
            'physical_defense': 1,
            'special_attack': 1,
            'special_defense': 4,
            'speed': 2
        }
    },
    {
        'model': 'team.player',
        'pk': 8,
        'fields': {
            'player_name': 'Jerry',
            'player_points': 26,
            'player_team': 2,
            'player_special_select': True,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 1,
            'physical_defense': 1,
            'special_attack': 9,
            'special_defense': 1,
            'speed': 1
        }
    },
    {
        'model': 'team.player',
        'pk': 9,
        'fields': {
            'player_name': 'Isaac',
            'player_points': 77,
            'player_team': 2,
            'player_special_select': True,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 1,
            'physical_defense': 1,
            'special_attack': 5,
            'special_defense': 1,
            'speed': 5
        }
    },
    {
        'model': 'team.player',
        'pk': 10,
        'fields': {
            'player_name': 'Patrick',
            'player_points': 25,
            'player_team': 2,
            'player_special_select': False,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 2,
            'physical_defense': 6,
            'special_attack': 1,
            'special_defense': 2,
            'speed': 1
        }
    }
]

team_fixtures = [
    {
        'model': 'team.team',
        'pk': 1,
        'fields': {
            'team_name': 'The Eagles',
            'team_points': 98
        }
    },
    {
        'model': 'team.team',
        'pk': 2,
        'fields': {
            'team_name': 'Team Super Strong',
            'team_points': 48
        }
    },
    {
        'model': 'team.team',
        'pk': 1,
        'fields': {
            'team_name': 'We Love Rice',
            'team_points': 21
        }
    },
    {
        'model': 'team.team',
        'pk': 2,
        'fields': {
            'team_name': 'Rice is Bae',
            'team_points': 56
        }
    },
    {
        'model': 'team.team',
        'pk': 1,
        'fields': {
            'team_name': 'RCSS Pride',
            'team_points': 74
        }
    },
    {
        'model': 'team.team',
        'pk': 2,
        'fields': {
            'team_name': 'Sleepy Nation',
            'team_points': 11
        }
    },
    {
        'model': 'team.team',
        'pk': 1,
        'fields': {
            'team_name': 'TTPS',
            'team_points': 21
        }
    },
    {
        'model': 'team.team',
        'pk': 2,
        'fields': {
            'team_name': 'How you doing?',
            'team_points': 82
        }
    },
    {
        'model': 'team.team',
        'pk': 1,
        'fields': {
            'team_name': 'The Destroyers',
            'team_points': 51
        }
    },
    {
        'model': 'team.team',
        'pk': 2,
        'fields': {
            'team_name': 'Wookieeeeee',
            'team_points': 23
        }
    },
]

with open('team/fixtures/fixtures.json', 'w') as outfile:
    json.dump(todo_fixtures + team_fixtures + player_fixtures, outfile)