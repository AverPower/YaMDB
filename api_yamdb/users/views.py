from rest_framework import viewsets

from api.models import User
from api.permissions import RolePermission, CurrentUserPermission
from .seriliazers import UserSeriliazer
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSeriliazer
    permission_classes = [RolePermission]
    filter_backends = (filters.SearchFilter, )
    search_fields = ['username']
    permission_groups = {
        'list': ['admin'],
        'create': ['admin'],
        'retrieve': ['admin'],
        'partial_update': ['admin'],
        'destroy': ['admin']
    }


class UserMeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSeriliazer

    def get_permissions(self):
        if self.action in ['retrieve', 'partial_update']:
            permission_classes = [CurrentUserPermission]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
