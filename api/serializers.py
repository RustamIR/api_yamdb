from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from users.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("username",
                  "pk",
                  "first_name",
                  "last_name",
                  "email",
                  "role",
                  "bio")


class EmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Users
        fields = ('email',)


class EmailCodeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=30)

    class Meta:
        model = Users
        fields = ('email', 'code')
