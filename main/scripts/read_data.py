import csv
import datetime
from decimal import Decimal

def make_objects(infile, coin):
    in_file = open(infile, 'r')
    in_reader = csv.reader(in_file)
    for row in in_reader:
        created = datetime.datetime.strptime(row[0], "%b %d, %Y").date()
        try:
            price = Decimal(row[1])
        except:
            price = 0
        try:
            high = Decimal(row[2])
        except:
            high = 0
        try:
            low = Decimal(row[3])
        except:
            low = 0
        try:
            close = Decimal(row[4])
        except:
            close = 0
        try:
            volume = Decimal(row[5])
        except:
            volume = 0
        try:
            market_cap = Decimal(row[6])
        except:
            market_cap = 0
        try:
            old_coin = coin.objects.get(date=created)
            old_coin.delete()
        except:
            pass
        coin.objects.create(date=created, price=price, high=high, low=low, close=close, volume=volume, market_cap=market_cap)

def make_rates(infile):
    in_file = open(infile, 'r')
    in_reader = csv.reader(in_file)
    rate = None
    for row in in_reader:
        created = datetime.datetime.strptime(row[1], "%Y/%M/%d").date()
        if rate:
            while rate.date != created + datetime.timedelta(days=1):
                rate = Rate.objects.create(date=created + datetime.timedelta(days=1), eur_rate=rate.eur_rate, gbp_rate=rate.gbp_rate)
        eur_rate = Decimal(row[3])
        gbp_rate = Decimal(row[4])
        rate = Rate.objects.create(date=created, eur_rate=eur_rate, gbp_rate=gbp_rate)

def make_stocks(infile, object):
        in_file = open(infile, 'r')
        in_reader = csv.reader(in_file)
        stock = None
        for row in in_reader:
            created = datetime.datetime.strptime(row[0], "%Y-%M-%d").date()
            if stock:
                while stock.date != created + datetime.timedelta(days=1):
                    stock = object.objects.create(date=created + datetime.timedelta(days=1), price=stock.price)
            price = Decimal(row[1])
            stock = object.objects.create(date=created, price=price)
