from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet
from .views import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'api/v1/titles', views.TitlesViewSet)
router.register(r'api/v1/genres',  views.GenresViewSet)
router.register(r'api/v1/categories', views.CategoriesViewSet)



urlpatterns = [
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


