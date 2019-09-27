# Generated by Django 2.2.4 on 2019-09-27 01:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_component', models.IntegerField(default=0)),
                ('way', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('genres', models.CharField(max_length=500)),
                ('watch_count', models.IntegerField(default=0)),
                ('averagerate', models.IntegerField(default=0)),
                ('plot', models.CharField(default='', max_length=1000)),
                ('url', models.CharField(default='', max_length=500)),
                ('director', models.CharField(default='', max_length=500)),
                ('casting', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='M', max_length=10)),
                ('age', models.IntegerField(default=25)),
                ('occupation', models.CharField(max_length=200)),
                ('approval', models.BooleanField(default=False)),
                ('subscription', models.DateTimeField(default=datetime.datetime(2019, 9, 10, 13, 47, 43, 630123))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Cluster_Kmeans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('K3', models.IntegerField(default=0)),
                ('K4', models.IntegerField(default=0)),
                ('K5', models.IntegerField(default=0)),
                ('K6', models.IntegerField(default=0)),
                ('K7', models.IntegerField(default=0)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_cluster_Kmeans', to='api.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='User_Cluster_Hmeans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('H3', models.IntegerField(default=0)),
                ('H4', models.IntegerField(default=0)),
                ('H5', models.IntegerField(default=0)),
                ('H6', models.IntegerField(default=0)),
                ('H7', models.IntegerField(default=0)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_cluster_Hmeans', to='api.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='User_Cluster_EM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EM3', models.IntegerField(default=0)),
                ('EM4', models.IntegerField(default=0)),
                ('EM5', models.IntegerField(default=0)),
                ('EM6', models.IntegerField(default=0)),
                ('EM7', models.IntegerField(default=0)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_cluster_EM', to='api.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription_manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.IntegerField(default=0)),
                ('approval', models.BooleanField(default=False)),
                ('request_day', models.DateTimeField(auto_now_add=True)),
                ('apply_day', models.DateTimeField(auto_now=True)),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_sub', to='api.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('Timestamp', models.IntegerField()),
                ('MovieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_movie', to='api.Movie')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_rate', to='api.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Cluster_Kmeans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('K3', models.IntegerField(default=0)),
                ('K4', models.IntegerField(default=0)),
                ('K5', models.IntegerField(default=0)),
                ('K6', models.IntegerField(default=0)),
                ('K7', models.IntegerField(default=0)),
                ('MovieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_cluster_Kmeans', to='api.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Cluster_Hmeans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('H3', models.IntegerField(default=0)),
                ('H4', models.IntegerField(default=0)),
                ('H5', models.IntegerField(default=0)),
                ('H6', models.IntegerField(default=0)),
                ('H7', models.IntegerField(default=0)),
                ('MovieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_cluster_Hmeans', to='api.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Cluster_EM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EM3', models.IntegerField(default=0)),
                ('EM4', models.IntegerField(default=0)),
                ('EM5', models.IntegerField(default=0)),
                ('EM6', models.IntegerField(default=0)),
                ('EM7', models.IntegerField(default=0)),
                ('MovieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_cluster_EM', to='api.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='score_users',
            field=models.ManyToManyField(related_name='score_movies', through='api.Rate', to='api.Profile'),
        ),
        migrations.CreateModel(
            name='Matrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie1', to='api.Movie')),
                ('Movie10', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie10', to='api.Movie')),
                ('Movie2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie2', to='api.Movie')),
                ('Movie3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie3', to='api.Movie')),
                ('Movie4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie4', to='api.Movie')),
                ('Movie5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie5', to='api.Movie')),
                ('Movie6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie6', to='api.Movie')),
                ('Movie7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie7', to='api.Movie')),
                ('Movie8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie8', to='api.Movie')),
                ('Movie9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie9', to='api.Movie')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matrix_set', to='api.Profile')),
            ],
        ),
    ]
