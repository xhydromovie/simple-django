# Generated by Django 2.1.2 on 2018-11-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0006_auto_20181104_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='image_url',
            field=models.CharField(default=0, max_length=100),
        ),
    ]