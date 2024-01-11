from django.urls import path, include

from .views import SignUpAPIView, LoginAPIView

app_name = "api"

urlpatterns = [
    path('', include('titles.urls')),
    path('', include('reviews.urls')),
    path('auth/signup/', SignUpAPIView.as_view(), name="auth_signup"),
    path('auth/token/', LoginAPIView.as_view(), name='auth_token'),
    path('users/', include('users.urls'))
]
