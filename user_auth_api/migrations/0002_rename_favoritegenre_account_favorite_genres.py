# Generated by Django 4.0.3 on 2022-03-22 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='favoritegenre',
            new_name='favorite_genres',
        ),
    ]
