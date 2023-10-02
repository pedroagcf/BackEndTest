from rest_framework import status
from django.http import JsonResponse
from pandas import Series
from api.Repositories.DividendRepository import DividendRepository
from api.models import Dividend
from api.services.YahooFinance import YahooFinance
from api.utils.serializers import serialize_dividend

class DividendController:
    @staticmethod
    def check_dividends(symbol, date, amount):
        return Dividend.objects.filter(symbol=symbol, date=date, amount=amount).exists()

    @staticmethod
    def load_dividends(symbol, year):
        dividends = YahooFinance.fetch_dividends(symbol)
        if not isinstance(dividends, Series):
            return JsonResponse({"success": False, "error": f"The symbol {symbol} does not exist!"}, status=status.HTTP_404_NOT_FOUND)

        saved_dividends = []
        for date, amount in dividends.items():
            if not DividendController.check_dividends(symbol, date, amount):
                DividendRepository.save_dividend(symbol, date, amount)
                saved_dividends.append({"date": date, "value": amount})

        serialized_data = serialize_dividend(symbol, year)

        return JsonResponse({"success": True, "data": serialized_data}, status=status.HTTP_200_OK)

