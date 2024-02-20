from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# API patterns for Admin
urlpatterns = [
    path("", TemplateView.as_view(template_name="not-found.html"), name="not-found"),
    path(settings.ADMIN_URL, admin.site.urls),
]

# API patterns for Authorization
urlpatterns += [
    path(f"{settings.API_PREFIX}auth/", include("djoser.urls.jwt")),
]

# API patterns for Spectacular
urlpatterns += [
    path(f"{settings.API_PREFIX}schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        f"{settings.API_PREFIX}docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

# API patterns for Local Apps
urlpatterns += [
    path(f"{settings.API_PREFIX}users/", include("apps.users.api.urls")),
    path(f"{settings.API_PREFIX}products/", include("apps.products.api.urls")),
    path(f"{settings.API_PREFIX}orders/", include("apps.orders.api.urls")),
    path(f"{settings.API_PREFIX}carts/", include("apps.carts.api.urls")),
]
