from django.contrib import admin
from django.urls import path, include

from .swagger import swagger_patterns

api_v1_urlpatterns = [
    path('swagger/', include(swagger_patterns)),
    path('products/', include('products.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1_urlpatterns)),
]
