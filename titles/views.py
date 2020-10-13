from requests import Response
from rest_framework import generics, mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Categories, Genres, Titles
from .serializers import (CategoriesSerializer, GenresSerializer,
                          TitlesSerializer)
from api.permissions import IsModerator, IsOwner, ReadOnly, AdminPermissions, TitleAdmin
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from titles.filters import TitlesFilter


class CustomListViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoriesViewSet(CustomListViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (TitleAdmin,)
    filter_backends = [SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'


class GenresViewSet(CustomListViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (TitleAdmin,)
    filter_backends = [SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'


class TitlesViewSet(
    CustomListViewSet
):
    pagination_class = PageNumberPagination
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (TitleAdmin,)
    filter_backends = [DjangoFilterBackend]
    filter_class = TitlesFilter

    def retrieve(self, request, serializer, titles_id):
        title = Titles.objects.get(titles_id=titles_id)
        serializer = TitlesSerializer(title)
        return Response(serializer.data)


