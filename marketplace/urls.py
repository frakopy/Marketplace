from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # paths to views
    path("", include("core.urls")),
    path("items/", include("item.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("conversation/", include("conversations.urls")),
    # paths to admin
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
