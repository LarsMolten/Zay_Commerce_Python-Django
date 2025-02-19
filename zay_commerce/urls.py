from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zay.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)