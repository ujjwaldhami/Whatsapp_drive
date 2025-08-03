import os
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from twilio.request_validator import RequestValidator
from core.utils.parser import parse_command
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


TWILIO_AUTH_TOKEN = "your_actual_twilio_auth_token_here"

def is_valid_twilio_request(request):
    validator = RequestValidator(TWILIO_AUTH_TOKEN)
    signature = request.headers.get("X-Twilio-Signature", "")
    url = request.build_absolute_uri()
    post_vars = request.POST.dict()
    return validator.validate(url, post_vars, signature)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def whatsapp_webhook(request):
    if not is_valid_twilio_request(request):
        return Response({"error": "Unauthorized Twilio request"}, status=status.HTTP_403_FORBIDDEN)

    command = request.data.get("Body", "").strip()

    if not command:
        return Response({"error": "No command received"}, status=status.HTTP_400_BAD_REQUEST)

    message = parse_command(command)  

    command_upper = command.upper()
    response_text = ""

    if command_upper.startswith("LIST"):
        folder = command[5:]
        response_text = f"📁 Listing files in: {folder}"

    elif command_upper.startswith("DELETE"):
        parts = command.split(" ", 1)
        if len(parts) > 1:
            response_text = f"🗑️ Deleting: {parts[1]}"
        else:
            response_text = "❌ Please specify what to delete."

    elif command_upper.startswith("MOVE"):
        parts = command.split(" ", 1)
        if len(parts) > 1:
            args = parts[1].split(" ")
            if len(args) == 2:
                response_text = f"📂 Moving {args[0]} → {args[1]}"
            else:
                response_text = "❌ Usage: MOVE <file> <destination>"
        else:
            response_text = "❌ Please specify what to move."

    elif command_upper.startswith("SUMMARY"):
        folder = command[8:]
        response_text = f"📝 Generating summary for: {folder}"

    else:
        response_text = f"⚠️ Unknown command: {command}"

    return Response({"message": response_text}, status=status.HTTP_200_OK)

def serve_frontend(request):
    file_path = os.path.join("frontend", "index.html")
    
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return HttpResponse(f.read(), content_type="text/html")
    else:
        return HttpResponse("Frontend not found", status=404)

def is_valid_twilio_request(request):
    if os.environ.get("DEBUG", "") == "1":
        return True  
    
