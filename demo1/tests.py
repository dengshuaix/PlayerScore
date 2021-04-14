from django.test import TestCase

# Create your tests here.
from demo1 import models


class ModelTest(TestCase):

    def test_search_score(self):
        import os

        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PlayerScore.settings')
        import django

        django.setup() # 启动django ORM
        start=1
        end=2
        all_customers = models.PlayerScoreRanking.objects.all().order_by('-grade')[int(start) - 1:int(end)]

        self.assertEquals(len(all_customers), 1)
