# Generated by Django 2.1.2 on 2018-11-09 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0013_smartphone_memory'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='cons',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='pros',
            field=models.CharField(default='', max_length=200),
        ),
    ]