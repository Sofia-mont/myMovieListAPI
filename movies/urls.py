from rest_framework import routers
from .api import ActorsViewSet, GenresViewSet, MoviesViewSet, DirectorsViewSet

router = routers.DefaultRouter()
router.register('movies',MoviesViewSet, 'movies')
router.register('directors',DirectorsViewSet, 'directors')
router.register('genres',GenresViewSet, 'genres')
router.register('actors',ActorsViewSet, 'actors')


urlpatterns = router.urls