from django.urls import path

from .views import SignUpAPIView, LoginAPIView, TestView

app_name = "api"

urlpatterns = [
    path('auth/signup/', SignUpAPIView.as_view(), name="auth_signup"),
    path('auth/token/', LoginAPIView.as_view(), name='auth_token'),
    path('check/', TestView.as_view())
    # path('users/me/', , name='auth_user_update'),
]
