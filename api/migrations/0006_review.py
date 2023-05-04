# Generated by Django 4.2 on 2023-04-23 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_flashcard_deck'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_attempts', models.IntegerField(default=0)),
                ('incorrect_attempts', models.IntegerField(default=0)),
                ('flashcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.flashcard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customuser')),
            ],
        ),
    ]
