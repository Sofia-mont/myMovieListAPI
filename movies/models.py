from django.db import models

# Create your models here.
class Directors(models.Model):
    name = models.CharField(max_length=300)
    dateBirth = models.DateField(auto_now=False, auto_now_add=False)
    placeBirth = models.CharField(max_length=200)

class Actors(models.Model):
    name = models.CharField(max_length=300)
    dateBirth = models.DateField(auto_now=False, auto_now_add=False)
    placeBirth = models.CharField(max_length=200)

class Genres(models.Model):
    genre = models.CharField(max_length=150)
    class Meta:
        verbose_name='genre'
        verbose_name_plural = 'genres'
        db_table='genres'
    def __str__(self):
        return self.genre
    
class Movies(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='movies')
    directer_by = models.ManyToManyField(Directors)
    cast = models.ManyToManyField(Actors)
    country = models.CharField(max_length=200)
    language =models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genres)
    synopsis = models.TextField(blank=True, null= True)
    release= models.DateField()

    class Meta:
        verbose_name='movie'
        verbose_name_plural = 'movies'
        db_table='movies'
    def __str__(self):
        return self.name