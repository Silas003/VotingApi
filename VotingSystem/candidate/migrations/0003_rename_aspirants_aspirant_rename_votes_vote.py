# Generated by Django 4.2.5 on 2023-09-13 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_votes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aspirants',
            new_name='Aspirant',
        ),
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
    ]