# Generated by Django 5.0.4 on 2024-05-07 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_performance_emp_delete_performance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]