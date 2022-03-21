<<<<<<< HEAD
# Generated by Django 4.0.3 on 2022-03-21 16:02
=======
# Generated by Django 4.0.3 on 2022-03-21 16:22
>>>>>>> ade889f3814389121a1cb8de55d9036d73d66240

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='default@gmail.com', max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, default='unknown', max_length=100)),
                ('favoritegenre', models.CharField(blank=True, choices=[('pop', 'Pop'), ('rock', 'Rock'), ('techno', 'Techno'), ('hiphop', 'Hip-hop'), ('jazz', 'Jazz'), ('rap', 'Rap'), ('country', 'Country'), ('metal', 'Metal'), ('alternative', 'Alternative'), ('indie', 'Indie')], default='', max_length=100)),
                ('image', models.CharField(blank=True, default='https://imgur.com/V4RclNb', max_length=100)),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to='user_auth_api.useraccount')),
            ],
        ),
    ]
