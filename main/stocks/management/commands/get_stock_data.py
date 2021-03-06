from django.core.management.base import BaseCommand, CommandErro
from django.conf import settings

from main.stocks.models import AAPL, AMZN, FB, GOOG, NFLX, MSFT, SPX, FANG, FAMGA
import requests
import datetime
import decimal

class Command(BaseCommand):
    help = 'Gets todays BTC price and saves it to the database'
    STOCKS = {AAPL: 'AAPL',
              AMZN: 'AMZN',
              FB: 'FB',
              GOOG: 'GOOG',
              NFLX: 'NFLX',
              MSFT: 'MSFT',
              SPX: 'SPX'}

    def handle(self, *args, **options):
        base_url = 'http://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}'
        fang = []
        famga = []
        for stock, symbol in self.STOCKS.items():
            request_json = requests.get(base_url.format(symbol, settings.ALPHA_VANTAGE_API_KEY)).json()
            previous_close = request_json['Realtime Global Securities Quote']['07. Close (Previous Trading Day)']
            date = datetime.date.today() - datetime.timedelta(days=1)
            
            if stock != AMZN or stock != MSFT:
                fang.append(decimal.Decimal(previous_close))
            if stock != NFLX:
                famga.append(decimal.Decimal(previous_close))

            model = stock(date=date, price=previous_close)
            model.save()
        
        
        FANG.objects.create(date=date, price=sum(fang))
        FAMGA.objects.create(date=date, price=sum(famga))
        self.stdout.write(self.style.SUCCESS('Successfully created stock price records!'))
