from datetime import datetime
from api.models import Dividend

def serialize_dividend(symbol, year):
    dividends = Dividend.objects.filter(symbol=symbol)
    total_amount = 0

    for dividend in dividends:
        year_db = datetime.strptime(str(dividend.date), "%Y-%m-%d %H:%M:%S%z").year
        if year_db == int(year):

            total_amount += round(dividend.amount, 3)

    return {"year": year, "amount": str(total_amount)}
