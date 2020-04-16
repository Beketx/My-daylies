from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=120)
    height = models.IntegerField()
    def __str__(self):
        return self.name

class Ball(models.Model):
    title = models.CharField(max_length=120)
    size = models.IntegerField()
    player_id = models.ForeignKey('Player',related_name="balls", on_delete=models.CASCADE)
    def __str__(self):
        return self.title