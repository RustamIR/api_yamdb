from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet
from ..users.views import AuthToken, AuthEmail

router = DefaultRouter()
router.register(r'v1/titles', TitlesViewSet)
router.register(r'v1/genres',  GenresViewSet)
router.register(r'v1/categories', CategoriesViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', AuthToken.as_view(), name='token_obtain_pair'),
    path('v1/token/email/', AuthEmail.as_view(), name='confirmation_code'),
] 

