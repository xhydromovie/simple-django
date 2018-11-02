from django.db import models

class Smartphone(models.Model):
    name = models.CharField(max_length=100)
    screen_size = models.FloatField()
    resolution_x = models.IntegerField()
    resolution_y = models.IntegerField()
    weight = models.FloatField()
    cpu = models.CharField(max_length=40)
    gpu = models.CharField(max_length=40)
    ram = models.IntegerField()

    def __str__(self):
        return self.name

