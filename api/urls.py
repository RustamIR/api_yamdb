from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, AuthEmail, AuthToken
from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
#router.register(r'genres', )
#router.register(r'categories', )
router.register(r'titles', TitleViewSet)


urlpatterns = [
    url('v1/', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]