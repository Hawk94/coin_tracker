from django.core.management.base import BaseCommand, CommandError
from main.coins.models import BTC, ETH, LTC
from core.utils import save_to_s3, model_to_json

import requests
import datetime


class Command(BaseCommand):
    help = 'Dumps all coin data to S3'

    def handle(self, *args, **options):
        models = [BTC, ETH, LTC]
        
        for model in models:
            json = model_to_json(model)
            save_to_s3(file_name=model.__name__, body=json)

        self.stdout.write(self.style.SUCCESS('Successfully saved coins to S3'))
