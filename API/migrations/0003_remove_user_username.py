# Generated by Django 4.1.2 on 2022-10-08 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
