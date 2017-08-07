from django.core.management.base import BaseCommand, CommandError
from main.coins.models import BTC, ETH, LTC
from main.rates.models import Rate
from main.stocks.models import AAPL, AMZN, FB, GOOG, NFLX, MSFT, SPX, FANG, FAMGA
from core.utils import save_to_s3, model_to_json

import requests
import datetime


class Command(BaseCommand):
    help = 'Dumps all coin data to S3'

    def handle(self, *args, **options):
        models = [BTC, ETH, LTC, AAPL, AMZN, FB, GOOG, NFLX, MSFT, SPX, FANG, FAMGA, Rate]

        json = model_to_json(models)
        save_to_s3(file_name='dustapp_data.json', body=json)

        self.stdout.write(self.style.SUCCESS('Successfully saved coins to S3'))
