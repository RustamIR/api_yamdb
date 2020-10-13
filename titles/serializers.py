from rest_framework import serializers
from .models import Titles, Categories, Genres
import datetime


class TitleCreateSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(slug_field='slug', many=True,
                                         queryset=Genres.objects.all())
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Categories.objects.all())

    class Meta:
        fields = ('id', 'name', 'year', 'genre', 'category', 'description')
        model = Titles


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Categories


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genres


class TitleListSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True)
    category = CategoriesSerializer()
    rating = serializers.FloatField()

    class Meta:
        fields = (
            'id', 'name', 'year', 'genre',
            'rating', 'category', 'description')
        model = Titles
