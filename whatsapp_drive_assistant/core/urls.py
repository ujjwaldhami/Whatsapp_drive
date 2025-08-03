from django.urls import path
from .views import whatsapp_webhook, serve_frontend

urlpatterns = [
    path("api/whatsapp-webhook/", whatsapp_webhook, name="whatsapp-webhook"),
    path('', serve_frontend),
]
