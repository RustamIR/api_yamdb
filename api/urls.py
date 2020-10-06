from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, AuthEmail, AuthToken
from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

#router.register(r'genres', )
#router.register(r'categories', )
router.register(r'titles', TitleViewSet)



urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', AuthToken.as_view(),
         name='token_obtain_pair'),
    path('v1/auth/email', AuthEmail.as_view(),
         name='confirmation_code'),
]