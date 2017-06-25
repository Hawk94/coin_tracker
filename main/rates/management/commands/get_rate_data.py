from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from main.rates.models import Rate
import requests
import datetime
import decimal

class Command(BaseCommand):
    help = 'Gets todays BTC price and saves it to the database'

    def handle(self, *args, **options):
        base_url = 'https://openexchangerates.org/api/latest.json?app_id={}'
        request_json = requests.get(base_url.format(settings.OPEN_EXCHANGE_APP_ID)).json()['rates']
        eur_rate = 1 / request_json['EUR']
        gbp_rate = 1 / request_json['GBP']
        date = datetime.date.today()

        Rate.objects.create(date=date, eur_rate=eur_rate, gbp_rate=gbp_rate)
        self.stdout.write(self.style.SUCCESS('Successfully created exchange rate records!'))
