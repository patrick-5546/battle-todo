from django.core.management.base import BaseCommand, CommandError
from team.models import Team, Player
from todo.models import Todo, Task

class Command(BaseCommand):
    help = 'Deletes all Team, Player, Todo, and Tasks objects'


    def handle(self, *args, **options):
        Team.objects.all().delete()
        Player.objects.all().delete()
        Todo.objects.all().delete()
        Task.objects.all().delete()
        self.stdout.write('Successfully deleted all model objects in database')