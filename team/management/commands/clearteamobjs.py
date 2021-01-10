from django.core.management.base import BaseCommand, CommandError
from team.models import Team, Player

class Command(BaseCommand):
    help = 'Deletes all Team and Player objects'


    def handle(self, *args, **options):
        Team.objects.all().delete()
        Player.objects.all().delete()
        self.stdout.write('Successfully deleted all Team and Player objects')