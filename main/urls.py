from django.urls import path

from django.conf import settings
from main.apps import AppConfig
from main.views import home, contacts
from django.conf.urls.static import static

app_name = AppConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)