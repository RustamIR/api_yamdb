from rest_framework import filters, generics, mixins, permissions, viewsets
from api.models import Review
from api.serializers import ReviewSerializer
from api.permissions import IsModerator, IsOwner, ReadOnly, AdminPermissions


class ReviewViewSet(viewsets.ModelViewSet):
    """
     Изменятьe/удалять могут только модеры,админ,автор
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (ReadOnly | IsOwner | IsModerator | AdminPermissions,)

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