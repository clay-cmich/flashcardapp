# Generated by Django 4.2 on 2023-04-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='total_cards_reviewed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='unique_cards_reviewed',
            field=models.IntegerField(default=0),
        ),
    ]
