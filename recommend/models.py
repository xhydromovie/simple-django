from django.db import models

class Smartphone(models.Model):
    name = models.CharField(max_length=100)
    screen_size = models.FloatField()
    resolution_x = models.IntegerField()
    resolution_y = models.IntegerField()
    battery = models.CharField(max_length=10, default=0)
    cpu = models.CharField(max_length=100)
    gpu = models.CharField(max_length=40)
    ram = models.IntegerField()
    memory = models.CharField(max_length=20, default=0)
    is_jack = models.CharField(max_length=15, default='Yes')
    system = models.CharField(max_length=8, default='android')
    pros = models.CharField(max_length=200, default='')
    cons = models.CharField(max_length=200, default='')
    fit = models.IntegerField(default=0)
    size = models.CharField(max_length=7, default='medium')
    price = models.IntegerField(default=0)
    image_url = models.CharField(max_length=100, default='')
    review_url_1 = models.CharField(max_length=200, default='')
    review_url_2 = models.CharField(max_length=200, default='')
    review_url_3 = models.CharField(max_length=200, default='')
    camera_rate = models.IntegerField(default=5)
    battery_rate = models.IntegerField(default=5)
    efficient_rate = models.IntegerField(default=5)
    display_rate = models.IntegerField(default=5)
    dimensions = models.CharField(default='', max_length=30)
    

    def __str__(self):
        return self.name

