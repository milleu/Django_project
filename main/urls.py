from django.urls import path

from main.apps import AppConfig
from main.views import home, contacts

app_name = AppConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]