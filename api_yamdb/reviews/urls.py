from django.urls import path, include

from rest_framework_nested import routers

from reviews.views import ReviewViewSet, CommentViewSet
from titles.urls import router


app_name = 'reviews'

review_router = routers.NestedDefaultRouter(router, r'titles', lookup='title')
review_router.register(r'reviews', ReviewViewSet)

comment_router = routers.NestedDefaultRouter(review_router, r'reviews', lookup='review')
comment_router.register(r'comments', CommentViewSet)

# router.register(r'titles/(?P<title_id>[\d]+)/reviews', ReviewViewSet)
# router.register(r'titles/(?P<title_id>[\d]+)/comments', CommentViewSet)


urlpatterns = [
    path('', include(review_router.urls)),
    path('', include(comment_router.urls))
]
