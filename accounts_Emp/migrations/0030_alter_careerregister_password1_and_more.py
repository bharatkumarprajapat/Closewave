# Generated by Django 5.0.4 on 2024-05-20 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_Emp', '0029_alter_careerregister_password1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerregister',
            name='password1',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='careerregister',
            name='password2',
            field=models.IntegerField(max_length=1000),
        ),
    ]
