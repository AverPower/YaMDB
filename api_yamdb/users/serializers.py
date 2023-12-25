import re
from rest_framework import serializers

from api.models import User


class UserSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')

    def validate_username(self, value: str):
        if not re.match(r'^[\w.@+-]+\z', value):
            return serializers.ValidationError(
                "Your username must be less than 150 charactesr and contain letters, digits and @/./+/-/_ only"
            )
        return True
