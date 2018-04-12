from django.db import models

# Create your models here.


class Player(models.Model):
    first_name = models.CharField(max_length = 50)
    user_name  = models.CharField(max_length = 50)
    last_name  = models.CharField(max_length = 50)


class LobbyMatch(models.Model):
    date_occured = models.DateField()
    players = models.ManyToManyField(Player)
