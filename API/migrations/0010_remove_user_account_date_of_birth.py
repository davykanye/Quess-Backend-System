# Generated by Django 4.1.2 on 2022-10-13 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0009_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_account',
            name='date_of_birth',
        ),
    ]
