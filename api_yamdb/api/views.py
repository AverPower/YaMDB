from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import User
from .serializers import SignUpSerializer, LoginSerializer
from .utils import generate_confirmation_code


class SignUpAPIView(APIView):

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            code = generate_confirmation_code(serializer.validated_data['username'])
            send_mail(
                subject='Registration YaMDB',
                message=f'Your verification code is {code}',
                from_email='yambd_noanswer@ya.ru',
                recipient_list=[serializer.validated_data['email']]
            )
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TestView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

