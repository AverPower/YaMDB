from rest_framework import serializers

from .models import User
from .utils import check_confirmation_code


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, write_only=True)
    confirmation_code = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, attrs):
        username = attrs.get('username', None)
        confirmation_code = attrs.get('confirmation_code', None)
        if username is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if confirmation_code is None:
            raise serializers.ValidationError(
                'A confirmation code is required to log in.'
            )
        user = User.objects.get(username=username)
        if user is None:
            raise serializers.ValidationError(
                'A user with this name was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        if not check_confirmation_code(confirmation_code, user.username):
            raise serializers.ValidationError(
                'You sent wrong verification code'
            )

        return {
            'token': user.token
        }
