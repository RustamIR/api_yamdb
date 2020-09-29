from rest_framework import viewsets, serializers, filters, generics, status
from users.models import Users
from api.serializers import UserSerializer
from api.permissions import AdminPermissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response




class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = AdminPermissions

    @action(detail=True, methods=['PATCH', 'GET'], url_name='user_profile',
            permission_classes=(IsAuthenticated,))
    def my_profile(self, request,):
        serializer = UserSerializer(request.user,
                                    data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class AuthEmail(generics.CreateAPIView):
    permission_classes = (AllowAny,)


class AuthToken(generics.CreateAPIView):
    permission_classes = (AllowAny,)
