from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
#from .models import Comment
from users.models import Users



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    post = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        fields = '__all__'
   #     model = Comment


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    user = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Users
        fields = '__all__'





