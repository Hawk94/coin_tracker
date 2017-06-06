from django.core.management.base import BaseCommand, CommandError
from main.coins.models import BTC

import requests
import datetime


class Command(BaseCommand):
    help = 'Gets todays BTC price and saves it to the database'

    def handle(self, *args, **options):
        url = 'http://api.coindesk.com/v1/bpi/historical/close.json?for=yesterday'
        request_json = requests.get(url).json()
        date, price = request_json['bpi']

        btc = BTC(date=datetime.datetime.strptime(date, '%Y-%m-%d').date(), price=price, excahnge='coindesk')
        btc.save()

        self.stdout.write(self.style.SUCCESS('Successfully created btc price record "%s"' % btc))
