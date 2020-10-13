from rest_framework import viewsets, serializers, filters, generics, status
from users.models import Users
from api.serializers import UserSerializer, EmailSerializer, \
    EmailCodeSerializer
from api.permissions import AdminPermissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination
import secrets
from django.contrib.auth.tokens import default_token_generator


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsAuthenticated, AdminPermissions,)

    @action(detail=False, methods=['PATCH', 'GET'],
            permission_classes=(IsAuthenticated,))
    def me(self, request, ):
        serializer = UserSerializer(request.user,
                                    data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthEmail(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        serializer = EmailSerializer(data={'email': email})
        serializer.is_valid(raise_exception=True)
        user, created = Users.objects.get_or_create(
            username=email, email=email)
        confirm_code = default_token_generator.make_token(user)
        send_mail(
            'Registration',
            'Your confirmation code is ' + str(confirm_code),
            [str(email)],
            fail_silently=False,
        )
        return Response("Ваш код ")


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class AuthToken(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def create(self, request):
        email = request.data.get('email')
        code = request.data.get('confirm_code')
        serializer = EmailCodeSerializer(data={'email': email, 'code': code})
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(Users, email=email)

        if not default_token_generator.check_token(user, code):
            raise ValidationError('Неверный код подтверждения!')

        token = get_tokens_for_user(user).get('access')

        return Response({'token': token})
