# Generated by Django 5.0.4 on 2024-05-13 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_Emp', '0019_chat_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('trainer', models.CharField(max_length=100)),
            ],
        ),
    ]
