# Generated by Django 4.1.2 on 2022-12-19 15:33

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_onetimelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='hash',
            field=models.CharField(default=accounts.models.generate_hash, max_length=64),
        ),
    ]
