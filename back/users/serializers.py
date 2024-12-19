from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},  # Password should be secure and write-only
        }

    def create(self, validated_data):
        """Create a new user with a hashed password."""
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],  # Password is automatically hashed by create_user
        )
        return user
