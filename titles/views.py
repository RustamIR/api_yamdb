from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Group, Follow
from .serializers import (CategoriesSerializer)
from .permissions import IsAuthorOrReadOnly
from rest_framework.filters import SearchFilter
from api.permissions import AdminPermissions, OwnReadOnly


class CategoriesAPIView(
    mixins.ListModelMixin,
    viewsets.DestroyViewSet
):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (permissions.IsAuthorOrReadOnly)
    filter_backends = [filters.SearchFilter]
    pagination_class = PageNumberPagination 
    search_fields = ['name'] 


class CategoriesAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (permissions.IsAuthenticated, AdminPermissions)
    filter_backends = [filters.SearchFilter]
    pagination_class = PageNumberPagination 
    search_fields = ['name'] 



class GenresAPIViewListAPIView(
    mixins.ListModelMixin, 
    generics.GenericAPIView
):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    filter_backends = [filters.SearchFilter]
    pagination_class = PageNumberPagination
    search_fields = ['name'] 


class GenresAPIViewListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (permissions.IsAuthenticated, AdminPermissions,)
    filter_backends = [filters.SearchFilter]
    pagination_class = PageNumberPagination
    search_fields = ['name'] 

class TitlesApiView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAuthorOrReadOnly)
    filter_backends = [filters.SearchFilter]
    pagination_class = PageNumberPagination 
    search_fields = ['name'] 


class TitlesApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (permissions.IsAuthenticated, AdminPermissions)
    filter_backends = [filters.SearchFilter]
    pagination_class = PageNumberPagination 
    search_fields = ['name'] 

