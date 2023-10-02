from api.controllers.DividendController import DividendController
from rest_framework import status
from django.http import JsonResponse, HttpResponse

def get_dividends(request, symbol, year):
    if request.method == "GET":
        
        response = DividendController.load_dividends(symbol, year)
        
        return response
    else:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
    