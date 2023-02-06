from .models import Directors, Actors, Genres, Movies
from .serializers import DirectorsSerializers, ActorsSerializers, GenresSerializers, MoviesSerializers
from rest_framework import viewsets, permissions

class DirectorsViewSet(viewsets.ModelViewSet):
    queryset = Directors.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DirectorsSerializers

class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actors.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ActorsSerializers

class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GenresSerializers

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MoviesSerializers