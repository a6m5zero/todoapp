#coding: utf-8
from django.core.management import BaseCommand
from datetime import datetime, timezone
from tasks.models import ToDoItem

class Command(BaseCommand):
    help = u"Insert task into DB from file('--filename')"

    def add_arguments(self, parser):
        parser.add_argument('--filename', dest='filename', type=str)

    def handle(self, *args, **options):
        with open(options['filename'], 'r') as file:
            for line in file:
                t = ToDoItem(descriprion = line)
                t.save()
            

        

            
            

        