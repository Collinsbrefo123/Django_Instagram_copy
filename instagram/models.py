from django.db import models


class InstaUsers(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
