# Generated by Django 4.1.2 on 2022-10-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_wallet_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=255, unique=True),
        ),
    ]
