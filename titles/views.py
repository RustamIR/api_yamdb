from requests import Response                                                                       
from rest_framework import viewsets, mixins, generics, status                                       
from rest_framework.permissions import IsAuthenticated                                              
from django_filters.rest_framework import DjangoFilterBackend                                       
from django.shortcuts import get_object_or_404                                                      
from rest_framework.decorators import action                                                        
from .models import Categories, Genres, Titles                                                      
from .serializers import (CategoriesSerializer, GenresSerializer, TitlesSerializer)                 
from .permissions import IsReadOnly                                                                 
from rest_framework.filters import SearchFilter                                                     
from ..api.permissions import AdminPermissions                                                      
from rest_framework.response import Response                                                        
from .permissions import IsAdminOrReadOnly                                                          
                                                                                                    
                                                                                                    
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
    permission_classes = (IsAuthenticated & IsAdminOrReadOnly | IsReadOnly)                         
    filter_backends = [SearchFilter]                                                                
    search_fields = ['name']                                                                        
                                                                                                    
#    @action(                                                                                       
 #       detail=True, methods=['POST', 'DELETE'],                                                   
  ###      permission_classes=IsAdminUser                                                           
   ### )                                                                                            
    ###def create(self, request, id):                                                               
     ##   if request.method == 'POST':                                                              
      #      serializer = CategoriesSerializer(data=request.data)                                   
       #     if serializer.is_valid():                                                              
       ##         serializer.save()                                                                 
       ##         return Response(serializer.data, status=status.HTTP_201_CREATED)                  
        #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                 
                                                                                                    
                                                                                                    
class GenresViewSet(CustomListViewSet):                                                             
    queryset = Genres.objects.all()                                                                 
    serializer_class = GenresSerializer                                                             
    permission_classes = (IsAuthenticated & IsAdminOrReadOnly | IsReadOnly)                         
    filter_backends = [SearchFilter]                                                                
    search_fields = ['name']                                                                        
                                                                                                    
#    @action(                                                                                       
 #       detail=True, methods=['POST', 'DELETE'],                                                   
  #      permission_classes=(permissions.IsAdminUser)                                               
   # )                                                                                              
    #def perform_create(request, id):                                                               
     #   genres = Genres.objects.get(id=id)                                                         
      #  if request.method == 'POST':                                                               
       #     serializer_class = GenresSerializer(data=request.data)                                 
        #    return Response(serializer.data, status=status.HTTP_200_OK)                            
#        elif request.method == 'DELETE':                                                           
 #           genres.delete()                                                                        
  #          return Response(status=status.HTTP_204_NO_CONTENT)                                     
   #     else:                                                                                      
    #        return Response(status=status.HTTP_403_FORBIDDEN)                                      
                                                                                                    
                                                                                                    
#class GenresAPIView(generics.RetrieveUpdateDestroyAPIView):                                        
 #   queryset = Genres.objects.all()                                                                
  #  serializer_class = GenresSerializer                                                            
   # permission_classes = (permissions.IsAuthenticated, AdminPermissions,)                          
    #filter_backends = [filters.SearchFilter]                                                       
    #search_fields = ['name']                                                                       
                                                                                                    
                                                                                                    
class TitlesViewSet(                                                                                
    CustomListViewSet                                                                               
):                                                                                                  
    queryset = Titles.objects.all()                                                                 
    serializer_class = TitlesSerializer                                                             
    permission_classes = (IsAuthenticated & IsAdminOrReadOnly | IsReadOnly)                         
    filter_backends = [DjangoFilterBackend]                                                         
    filterset_field = ['category__name', 'genre__name']                                             
                                                                                                    
    def retrieve(self, request, serializer, titles_id):                                             
        title = Titles.objects.get(titles_id=titles_id)                                             
        serializer = TitlesSerializer(title)                                                        
        return Response(serializer.data)                                                            
