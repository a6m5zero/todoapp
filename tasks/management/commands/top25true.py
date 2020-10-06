#coding: utf-8
from django.core.management import BaseCommand
from datetime import datetime, timezone
from tasks.models import ToDoItem
from django.contrib.auth.models import User
from collections import Counter 



class Command(BaseCommand):
    help = u"Display Top25 user with complited tasks"
    
    def add_arguments(self, parser):
        parser.add_argument('--t', dest='t', type=bool, default=False)
    
    def handle(self, *args, **options):
        top = []
        for user in User.objects.all():
            for task in user.tasks.all():
                if task.is_completed == options['t']:
                    top.append(user.username)
                else:
                    continue
        c = Counter(top)
        print(c.most_common(25))

        