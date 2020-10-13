from rest_framework import serializers
from .models import Titles, Categories, Genres
import datetime


class TitlesSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all())
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        many=True,
        queryset=Genres.objects.all())
    rating = serializers.FloatField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Titles

    def validate_year(self, year):
        current_year = datetime.date.today().year
        if year > current_year:
            raise serializers.ValidationError(
                'Год произведения не может быть больше текущего'
            )
        return year


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Categories


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genres
