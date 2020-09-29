from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'^posts', PostViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register(r'^group', GroupViewSet)
router.register(r'^follow', FollowViewSet)
router.register(r'^titles', TitleViewSet)


urlpatterns = [
    url('v1/', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]