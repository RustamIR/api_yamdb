from rest_framework import filters, generics, mixins, permissions, viewsets
from api.models import Review

class ReviewViewSet(viewsets.ModelViewSet):
    """
     Изменятьe/удалять могут только модеры,админ,автор
    """
    queryset = Review.objects.all()
    #serializer_class =
    #permission_classes =

    def get_queryset(self):
        """
        Необходимо вернуть только одзывы которые принадлежат конкретному произведению, по id например
        """
        title =

    def create(self):
        """
       создать новый отзыв
        """



class CommentViewSet(viewsets.ModelViewSet):
    """
    Суть та же что и с ревью
    """