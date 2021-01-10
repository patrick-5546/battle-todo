from django.contrib import admin

from .models import Team, Player

class PlayerInline(admin.StackedInline):
    fieldsets = [
        (None,               {'fields': ['player_name', 'player_points', 'player_special_select', 'has_attacked', 'damage_dealt', 'todo_points']}),
        ('Skills', {'fields': ['physical_attack', 'physical_defense', 'special_attack', 'special_defense',
                               'speed'], 'classes': ['collapse']}),
    ]
    model = Player
    extra = 1

class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]
    list_display = ('team_name', 'team_points')
    search_fields = ['team_name']

admin.site.register(Team, TeamAdmin)
