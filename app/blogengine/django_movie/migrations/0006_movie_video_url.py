# Generated by Django 5.0.6 on 2024-07-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_movie', '0005_alter_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video_url',
            field=models.CharField(default='https://www.youtube.com/', max_length=800, verbose_name='Трейлер'),
        ),
    ]