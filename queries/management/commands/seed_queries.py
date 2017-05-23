import random
from django.core.management.base import BaseCommand, CommandError
from faker import Factory
from queries.models import Query

class Command(BaseCommand):
  help = 'Initialize database with dummy info'

  def handle(self, *args, **options):
    fake = Factory.create('es_ES')

    for _ in range(0,5):
      oprtions = ['RE', 'OF']
      random.shuffle(oprtions)
      q = Query(intention=oprtions.pop())
      q.save()
      for _ in range(0,5):
        q.keywords.add(fake.first_name())
      q.save()
