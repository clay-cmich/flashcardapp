# Generated by Django 4.2 on 2023-04-16 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_customuser_bio_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='days_review',
            new_name='days_reviewed',
        ),
    ]