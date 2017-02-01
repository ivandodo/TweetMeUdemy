from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username='someRandomUser123456734562')

    def test_tweet_item(self):
        obj = Tweet.object.create(
            user=User.objects.first(),
            content='Random content'
        )

        self.assertTrue(obj.content == 'Random content')


