from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=100, blank=True)
    artist = models.CharField(max_length=100, blank=True)
    GENRE_CHOICES = [
        ('pop', 'Pop'),
        ('rock', 'Rock'),
        ('techno', 'Techno'),
        ('hiphop', 'Hip-hop'),
        ('jazz', 'Jazz'),
        ('rap', 'Rap'),
        ('country', 'Country'),
        ('metal', 'Metal'),
        ('alternative', 'Alternative'),
        ('indie', 'Indie'),
    ]
<<<<<<< HEAD
    genre = models.CharField(
        max_length=100, choices=GENRE_CHOICES, default='Pop', blank=True)
    audio = models.FileField(upload_to='uploads/')
    image = models.CharField(
        max_length=100, default='https://i.imgur.com/D3aOVsJ.png', blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default='1.29', blank=True)
=======
    genre = models.CharField(max_length = 100, choices=GENRE_CHOICES, default='', blank = True)
    audio = models.FileField(upload_to='uploads/')
    image = models.CharField(max_length = 100, default = 'https://i.imgur.com/D3aOVsJ.png', blank = True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default = '1.29', blank = True)
>>>>>>> ade889f3814389121a1cb8de55d9036d73d66240
