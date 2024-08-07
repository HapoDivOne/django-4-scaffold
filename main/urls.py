"""
URL configuration for micadoweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Ensure `include` is imported
from rest_framework import routers
from hotels.views import HotelViewSet
from django.urls import include, re_path
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView, TokenBlacklistView)

# Hotels router
hotels_router = routers.SimpleRouter()
hotels_router.register(
    r'hotels',
    HotelViewSet,
    basename='hotel',
)

schema_view = get_schema_view(
    openapi.Info(
        title="Django-4-scaffold Swagger",
        default_version='v1',),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # API
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/login', TokenObtainPairView.as_view(), name='login'),
    path('api/', include('users.urls')),
    path('api/', include(hotels_router.urls)),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
]

