from django.contrib.auth.models import User
from django.db import models

from rbt_rocks import settings


class BotCredentials(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    client_id = models.CharField(max_length=256)
    client_secret = models.CharField(max_length=256)
    date_added = models.DateTimeField('Date added', auto_now_add=True)

    def __str__(self):
        return f"{self.user}: ({self.username}:********), ({self.client_id}:********)"


class Target(models.Model):
    SUBREDDIT = 'SUBREDDIT'
    USERNAME = 'USERNAME'

    TYPE_CHOICES = [
        (SUBREDDIT, 'subreddit'),
        (USERNAME, 'username'),
    ]

    credentials = models.ForeignKey(BotCredentials, on_delete=models.CASCADE)
    type = models.CharField(max_length=256, choices=TYPE_CHOICES, default=SUBREDDIT)
    value = models.CharField(max_length=256)
    is_active = models.BooleanField(default=False)
    date_added = models.DateTimeField('Date added', auto_now_add=True)

    def __str__(self):
        return f"{self.type} '{self.value}' {'☑' if self.is_active else '☐' }"
