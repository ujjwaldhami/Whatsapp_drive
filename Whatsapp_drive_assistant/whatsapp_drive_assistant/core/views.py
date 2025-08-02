from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class WhatsAppWebhookView(APIView):
    def post(self, request, format=None):
        command = request.data.get("Body", "").strip()
        sender = request.data.get("From", "").strip()

        if not command or not sender:
            return Response({"error": "Missing 'Body' or 'From'"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": f"Command received: {command}"}, status=status.HTTP_200_OK)
