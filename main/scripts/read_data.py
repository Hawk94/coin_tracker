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
        