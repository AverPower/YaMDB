from django.db.models import Avg

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response

from api.permissions import RolePermission
from titles.serializers import TitleSerializer, GenreSerializer, CategorySerializer
from titles.models import Title, Genre, Category
from reviews.models import Review


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (RolePermission,)
    filter_backends = (DjangoFilterBackend,)
    pagination_class = PageNumberPagination
    filterset_fields = ('category__slug', 'name', 'year')
    permission_groups = {
        'list': ['anon'],
        'create': ['admin'],
        'retrieve': ['anon'],
        'partial_update': ['admin'],
        'destroy': ['admin']
    }

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        rating = int(Review.objects.filter(title=instance).aggregate(Avg('score', default=0))['score__avg'])
        instance.rating = rating
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


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
    pagination_class = PageNumberPagination
    search_fields = ['name']
    lookup_field = 'slug'
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
    pagination_class = PageNumberPagination
    search_fields = ['name']
    lookup_field = 'slug'
    permission_groups = {
        'list': ['anon'],
        'create': ['admin'],
        'destroy': ['admin']
    }
