from django.core.management.base import BaseCommand, CommandError
from main.coins.models import LTC

import requests
import datetime


class Command(BaseCommand):
    help = 'Gets todays BTC price and saves it to the database'

    def handle(self, *args, **options):
        url = 'https://min-api.cryptocompare.com/data/histoday?fsym=LTC&tsym=USD&limit=1&aggregate=1&e=CCCAGG'
        request_json = requests.get(url).json()
        data = request_json['Data'][-1]
        price = data['close']
        date = datetime.datetime.utcfromtimestamp(data['time'])

        ltc = LTC(date=date.date(), price=price, exchange='cryptocompare')
        ltc.save()

        self.stdout.write(self.style.SUCCESS('Successfully created btc price record "%s"' % ltc))
