from django.db import models

class GenreChoices(models.TextChoices):
    POP_MUSIC = 'Pop', 'Pop Music'
    JAZZ_MUSIC = 'Jazz', 'Jazz Music'
    RB_MUSIC = 'R&B', 'R&B Music'
    ROCK_MUSIC = 'Rock', 'Rock Music'
    COUNTRY_MUSIC = 'Country', 'Country Music'
    DANCE_MUSIC = 'Dance', 'Dance Music'
    HIP_HOP_MUSIC = 'Hip hop', 'Hip-hop Music'
    OTHER = 'Other', 'Other'
