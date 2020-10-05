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


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = AdminPermissions

    @action(detail=True, methods=['PATCH', 'GET'], url_name='user_profile',
            permission_classes=(IsAuthenticated,))
    def my_profile(self, request, ):
        serializer = UserSerializer(request.user,
                                    data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthEmail(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            if Users.objects.filter(email=email).exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                user = Users.objects.create(email=email)
                code = default_token_generator.make_token(user)
                send_mail(
                    'Ваш емейл не инвалид,держите код', code
                )
                return Response({code})


class AuthToken(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def create(self, request):
        email = request.data.get('email')
        code = request.data.get('confirmation_code')
        serializer = EmailCodeSerializer(data={'email': email, 'code': code})
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(Users, email=email)
        if not default_token_generator.check_token(user, code):
            raise ValidationError('Неверный код и я не про свой')

        return Response(("Твой токен: " + str(RefreshToken.for_user(user))))
