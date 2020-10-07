from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet
from .views import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'titles', views.TitlesViewSet)
router.register(r'genres',  views.GenresViewSet)
router.register(r'categories', views.CategoriesViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', AuthToken.as_view(), name='token_obtain_pair'),
    path('v1/token/email/', AuthEmail.as_view(), name='confirmation_code'),
] 

