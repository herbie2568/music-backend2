# Generated by Django 4.0.3 on 2022-03-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_api', '0002_alter_user_password_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]