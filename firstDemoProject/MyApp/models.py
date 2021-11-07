from django.db import models

# Create your models here.

class  Book(models.Model):

    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 300)
    price = models.IntegerField()

