from django.urls import path

from .views import webhook
urlpatterns = [
    path("bot/", webhook, name='webhook'),
    ]
