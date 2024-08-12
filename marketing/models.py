from django.db import models

class Market(models.Model):
    name = models.CharField( max_length=50)
    date = models.DateField()

