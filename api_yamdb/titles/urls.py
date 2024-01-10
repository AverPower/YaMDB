from django.urls import path, include

from rest_framework import routers

from .views import TitleViewSet, GenreViewSet, CategoryViewSet


app_name = 'titles'

router = routers.DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
