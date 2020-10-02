from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
#from .models import Comment
from users.models import Users






class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    user = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Users
        fields = '__all__'

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

