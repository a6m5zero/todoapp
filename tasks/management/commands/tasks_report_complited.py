#coding: utf-8
from django.core.management import BaseCommand
from datetime import datetime, timezone
from tasks.models import ToDoItem

class Command(BaseCommand):
    help = u"Display completed tasks in the last days' dates (DEFAULT = 3 days)"
    
    def add_arguments(self, parser):
        parser.add_argument('--days', dest='days', type=int, default=3)
    
    def handle(self, *args, **options):
        now = datetime.now(timezone.utc)
        for t in ToDoItem.objects.filter(is_completed=True):
            if (now - t.created).days <= options['days']:
                print("Выполнена задача:", t, t.created)