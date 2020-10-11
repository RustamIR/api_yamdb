from rest_framework import viewsets, mixins, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Categories, Genres, Titles
from .serializers import (CategoriesSerializer, GenresSerializer,
                          TitlesSerializer)
from titles.permissions import IsAdminOrReadOnly
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from .filters import TitlesFilter


class CustomListViewSet(
    mixins.CreateModelMixin,
    mixins.DeleteModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoriesViewSet(CustomListViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ['name']


class GenresViewSet(CustomListViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [SearchFilter]
    search_fields = ['name']


class TitlesViewSet(
    viewsets.ModelViewSet,
    CustomListViewSet
):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filter_class = TitlesFilter

    def retrieve(self, request, serializer, titles_id):
        title = Titles.objects.get(titles_id=titles_id)
        serializer = TitlesSerializer(title)
        return Response(serializer.data)
