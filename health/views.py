from django.db import connection
from django.http import JsonResponse
from rest_framework import status


def liveness(request):
    return JsonResponse({"status": "OK"})


def readiness(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")

        return JsonResponse({"status": "Ready!"})
    except Exception:
        return JsonResponse({"status": "not ready"}, status=503)
