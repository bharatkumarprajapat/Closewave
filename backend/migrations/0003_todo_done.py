# Generated by Django 5.0.4 on 2024-04-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]