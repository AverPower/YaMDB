from django.urls import path, include

from rest_framework import routers

from .views import UserViewSet, UserMeViewSet


app_name = 'users'

router = routers.DefaultRouter()

router.register(r'', UserViewSet)


urlpatterns = [
    path('me/', UserMeViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
    path('', include(router.urls)),
]
