from rest_framework.routers import DefaultRouter

from products.views import ProductCategoryViewSet


router = DefaultRouter()
router.register('categories', ProductCategoryViewSet)


urlpatterns = [] + router.urls
