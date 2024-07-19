# Generated by Django 5.0.6 on 2024-07-18 08:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quick_start', '0002_snippet_highlighted_snippet_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='highlighted',
            field=models.TextField(default='1'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippet', to=settings.AUTH_USER_MODEL),
        ),
    ]