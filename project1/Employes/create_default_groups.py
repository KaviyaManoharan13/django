from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Creates default Django groups'

    def handle(self, *args, **options):
        # Create default groups if they don't exist
        Group.objects.get_or_create(name='Administrators')
        Group.objects.get_or_create(name='Managers')
        Group.objects.get_or_create(name='Users')

        self.stdout.write(self.style.SUCCESS('Default Django groups created successfully.'))
