from rest_framework import serializers
from .models import Directors, Actors, Genres, Movies


class DirectorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Directors
        fields = ['id', 'name', 'dateBirth', 'placeBirth']

class ActorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = ['id', 'name', 'dateBirth', 'placeBirth']

class GenresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id', 'genre']

class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'name', 'poster', 'directer_by', 'cast', 'country', 'language', 'duration', 'genres', 'synopsis', 'release']