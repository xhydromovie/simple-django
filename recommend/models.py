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
    camera_rate = models.IntegerField(default=5)
    fit = models.IntegerField(default=0)
    system = models.CharField(max_length=8, default='android')
    size = models.CharField(max_length=7, default='medium')
    
    class Meta:
        ordering = ['fit']

    def __str__(self):
        return self.name

