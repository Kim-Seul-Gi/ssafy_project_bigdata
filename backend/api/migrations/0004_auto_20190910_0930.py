# Generated by Django 2.2.4 on 2019-09-10 00:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_movie_cluster_em_movie_cluster_hmeans_movie_cluster_kmeans_user_cluster_em_user_cluster_hmeans_user_'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='casting',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='movie',
            name='plot',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='movie',
            name='url',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='subscription',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 9, 9, 30, 50, 340063)),
        ),
    ]
