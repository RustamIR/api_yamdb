from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet



router = DefaultRouter()
router.register(r'^titles', TitleViewSet)
router.register(r'^genres', TitleViewSet)
router.register(r'^categories', TitleViewSet)


urlpatterns = [
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 