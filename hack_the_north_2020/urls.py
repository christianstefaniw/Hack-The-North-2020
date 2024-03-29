from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
