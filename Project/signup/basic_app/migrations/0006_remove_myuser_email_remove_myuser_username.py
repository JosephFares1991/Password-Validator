# Generated by Django 4.2.7 on 2023-11-11 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_remove_myuser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='username',
        ),
    ]