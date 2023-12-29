from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from api.permissions import RolePermission
from serializers import TitleSerializer, GenreSerializer, CategorySerializer
from models import Title, Genre, Category


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (RolePermission,)
    filter_backends = (DjangoFilterBackend,)
    pagination_class = PageNumberPagination
    filterset_fields = ('category__slug', 'genre__slug', 'name', 'year')
    permission_groups = {
        'list': ['anon'],
        'create': ['admin'],
        'retrieve': ['anon'],
        'partial_update': ['admin'],
        'destroy': ['admin']
    }


class GenreViewSet(
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.DestroyModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [RolePermission]
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name']
    permission_groups = {
        'list': ['anon'],
        'create': ['admin'],
        'destroy': ['admin']
    }


class CategoryViewSet(
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.DestroyModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [RolePermission]
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name']
    permission_groups = {
        'list': ['anon'],
        'create': ['admin'],
        'destroy': ['admin']
    }
