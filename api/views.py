from rest_framework import filters, generics, mixins, permissions, viewsets
from api.models import Review, Comment
from django.shortcuts import render, get_object_or_404
from api.serializers import ReviewSerializer, CommentSerializer
from api.permissions import IsModerator, IsOwner, ReadOnly, AdminPermissions
from titles.models import Titles


class ReviewViewSet(viewsets.ModelViewSet):
    """
     Изменятьe/удалять могут только модеры,админ,автор
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (ReadOnly | IsOwner | IsModerator | AdminPermissions,)

    def get_queryset(self):
        title = get_object_or_404(Titles, pk=self.kwargs.get('title_id'))
        return Review.objects.filter(title=title)

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles, pk=title_id)
        serializer.save(author=self.request.user, title_id=title.id)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Суть та же что и с ревью
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (ReadOnly | IsOwner | IsModerator | AdminPermissions,)

    def get_queryset(self):
        review_id = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return Comment.objects.filter(review=review_id)

    def perform_create(self, serializer):
        review_id = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review_id)
