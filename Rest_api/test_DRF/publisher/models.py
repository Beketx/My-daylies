from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    age = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.name




class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey('Author', related_name='books', on_delete = models.CASCADE)
    def __str__(self):
        return self.title