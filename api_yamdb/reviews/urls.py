from django.urls import path, include

from rest_framework import routers

from reviews.views import ReviewViewSet, CommentViewSet


app_name = 'reviews'

router = routers.DefaultRouter()

router.register(r'titles/(?P<title_id>[\d]+)/reviews', ReviewViewSet)
router.register(r'titles/(?P<title_id>[\d]+)/comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
