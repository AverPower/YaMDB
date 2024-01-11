from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from api.permissions import RolePermission
from reviews.serializers import ReviewSerializer, CommentSerializer
from titles.models import Title
from reviews.models import Review, Comment


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (RolePermission,)
    pagination_class = PageNumberPagination
    permission_groups = {
        'list': ['anon'],
        'create': ['user', 'moderator', 'admin'],
        'retrieve': ['anon'],
        'partial_update': ['user', 'moderator', 'admin'],
        'destroy': ['user', 'moderator', 'admin']
    }

    @staticmethod
    def mean(array: list):
        _sum = sum(array)
        _len = len(array)
        return _sum // _len

    def get_queryset(self):
        titled_id = self.kwargs["title_id"]
        title = get_object_or_404(Title, pk=titled_id)
        return self.queryset.filter(title=title)

    def create(self, request, *args, **kwargs):
        title = get_object_or_404(Title, pk=kwargs["title_id"])
        data = request.data
        data['title'] = title
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        title.rating = self.mean(self.get_queryset().values_list('score', flat=True))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (RolePermission,)
    pagination_class = PageNumberPagination
    permission_groups = {
        'list': ['anon'],
        'create': ['user'],
        'retrieve': ['anon'],
        'partial_update': ['user', 'moderator', 'admin'],
        'destroy': ['user', 'moderator', 'admin']
    }
