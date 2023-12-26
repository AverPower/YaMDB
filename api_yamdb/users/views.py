from rest_framework import viewsets

from api.models import User
from api.permissions import RolePermission, CurrentUserPermission
from .serializers import UserSeriliazer
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSeriliazer
    permission_classes = [RolePermission]
    filter_backends = (filters.SearchFilter, )
    search_fields = ['username']
    lookup_field = 'username'
    permission_groups = {
        'list': ['admin'],
        'create': ['admin'],
        'retrieve': ['admin'],
        'partial_update': ['admin'],
        'destroy': ['admin']
    }


class UserMeViewSet(viewsets.mixins.RetrieveModelMixin, viewsets.mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSeriliazer
    permission_classes = [CurrentUserPermission]

    def get_object(self):
        return self.request.user
