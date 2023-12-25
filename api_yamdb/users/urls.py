from django.urls import path, include

from rest_framework import routers

from .views import UserViewSet, user_me_view


app_name = 'users'

router = routers.DefaultRouter()

router.register(r'/(?P<user_id>^[\w.@+-]+\z)', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('me/', user_me_view.asview())
]
