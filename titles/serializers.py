from rest_framework import serializers
from .models import Titles, Categories, Genres


class TitlesSerializer(serializers.ModelSerializer):
    class Meta():
        fields ='__all__'
        model = Titles


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta():
        fields ='__all__'
        model = Categories


class Genres(serializers.ModelSerializer):
    class Meta():
        fields ='__all__'
        model = Genres
