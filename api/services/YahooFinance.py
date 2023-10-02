import yfinance as yf
class YahooFinance:
  @staticmethod
  def fetch_dividends(symbol):
      try:
          ticker = yf.Ticker(symbol)
          dividends = ticker.dividends
      except Exception as err:
          return {"success": False, "error_message": f"An error occurred: {str(err)}"}

      return dividends