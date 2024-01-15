from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from api.permissions import RoleAuthCurrentUserPermission
from reviews.serializers import ReviewSerializer, CommentSerializer
from titles.models import Title
from reviews.models import Review, Comment


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (RoleAuthCurrentUserPermission,)
    pagination_class = PageNumberPagination
    permission_groups = {
        'list': ['anon'],
        'create': ['user', 'moderator', 'admin'],
        'retrieve': ['anon'],
        'partial_update': ['user', 'moderator', 'admin'],
        'destroy': ['user', 'moderator', 'admin']
    }

    def get_queryset(self):
        get_object_or_404(Title, pk=self.kwargs["title_pk"])
        return Review.objects.filter(title=self.kwargs['title_pk'])

    def create(self, request, *args, **kwargs):
        title = Title.objects.get(pk=kwargs["title_pk"])
        data = request.data
        data['title'] = title
        data['author'] = request.user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (RoleAuthCurrentUserPermission,)
    pagination_class = PageNumberPagination
    permission_groups = {
        'list': ['anon'],
        'create': ['user'],
        'retrieve': ['anon'],
        'partial_update': ['user', 'moderator', 'admin'],
        'destroy': ['user', 'moderator', 'admin']
    }

    def get_queryset(self):
        get_object_or_404(
            Review,
            pk=self.kwargs["review_pk"],
            title__pk=self.kwargs["title_pk"]
        )
        return Comment.objects.filter(review=self.kwargs['review_pk'])

    def create(self, request, *args, **kwargs):
        review = Review.objects.get(pk=kwargs["review_pk"])
        data = request.data
        data['review'] = review
        data['author'] = request.user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
