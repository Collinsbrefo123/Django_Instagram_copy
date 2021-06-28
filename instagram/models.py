from django.db import models
from django.contrib.auth.models import User

class InstaUsers(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Feeds(models.Model):
    feedTitle = models.CharField(max_length=100, null=True)
    imgFeed = models.ImageField(upload_to='upload')
    caption = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.feedTitle

