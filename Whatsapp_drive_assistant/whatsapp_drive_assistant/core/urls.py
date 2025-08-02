from django.urls import path
from .views import WhatsAppWebhookView

urlpatterns = [
    path("api/whatsapp-webhook/", WhatsAppWebhookView.as_view(), name="whatsapp-webhook"),
]
