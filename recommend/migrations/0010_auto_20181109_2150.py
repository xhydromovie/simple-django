# Generated by Django 2.1.2 on 2018-11-09 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0009_smartphone_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='weight',
        ),
        migrations.AddField(
            model_name='smartphone',
            name='review_url_1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='review_url_2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='review_url_3',
            field=models.CharField(default='', max_length=200),
        ),
    ]