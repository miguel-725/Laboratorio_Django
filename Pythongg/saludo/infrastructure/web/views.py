import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from saludo.application.services.saludar_service import SaludarService

saludar_use_case = SaludarService()

@require_http_methods(["GET"])
def saludar_get(request, nombre):
    try:
        mensaje = saludar_use_case.ejecutar(nombre)
        return JsonResponse({"mensaje": mensaje})
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def saludar_post(request):
    try:
        data = json.loads(request.body)
        mensaje = saludar_use_case.ejecutar(data.get("nombre"))
        return JsonResponse({"mensaje": mensaje})
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido"}, status=400)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)