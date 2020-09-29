from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.views import UserViewSet, AuthEmail, AuthToken

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')



urlpatterns = [
    url('v1/', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]