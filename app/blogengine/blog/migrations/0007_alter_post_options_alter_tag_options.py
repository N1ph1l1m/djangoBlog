# Generated by Django 5.0.4 on 2024-06-04 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_worker_cat_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_pub']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title']},
        ),
    ]
