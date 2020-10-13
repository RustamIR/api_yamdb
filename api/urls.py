from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, AuthEmail, AuthToken

from api.views import CommentViewSet, ReviewViewSet
from titles.views import TitlesViewSet, CategoriesViewSet, GenresViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'titles', TitlesViewSet)
router.register(r'genres',  GenresViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewSet, basename='comments')





urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', AuthToken.as_view(),
         name='token_obtain_pair'),
    path('v1/auth/email', AuthEmail.as_view(),
         name='confirmation_code'),

]
