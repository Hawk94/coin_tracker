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

def make_FAMGA():
    start = datetime.datetime.strptime('2013-1-1', "%Y-%M-%d").date()
    end = datetime.datetime.strptime('2014-12-31', "%Y-%M-%d").date()
    delta = end - start
    for i in range(delta.days + 1):
        date = start + datetime.timedelta(days=i)
        try:
            aapl = AAPL.objects.filter(date=date).first().price
        except:
            aapl = 0
        try:
            amzn = AMZN.objects.filter(date=date).first().price
        except:
            amzn = 0
        try:
            fb = FB.objects.filter(date=date).first().price
        except:
            fb = 0
        try:
            goog = GOOG.objects.filter(date=date).first().price
        except:
            goog = 0
        try:
            msft = MSFT.objects.filter(date=date).first().price
        except:
            msft = 0
        prices = [aapl,
                  amzn,
                  fb,
                  goog,
                  msft]
        FAMGA.objects.create(date=date, price=decimal.Decimal(sum(prices)))

def clean_data(object):
    start = datetime.datetime.strptime('2013-1-1', "%Y-%M-%d").date()
    end = datetime.datetime.strptime('2017-8-9', "%Y-%M-%d").date()
    delta = end - start
    clean_first(object)
    for i in range(delta.days + 1):
        date = start + datetime.timedelta(days=i)
        try:
            all_objects = object.objects.filter(date=date)
            len_o = len(all_objects)
            for i in range(len_o-1):
                all_objects[i].delete()
        except:
            price = object.objects.filter(date=date-datetime.timedelta(days=1)).first().price
            object.objects.create(date=date, price=price)

def clean_first(object):
    date = datetime.datetime.strptime('2013-1-1', "%Y-%M-%d").date()
    all_objects = object.objects.filter(date=date)
    len_o = len(all_objects)
    for i in range(len_o-1):
        all_objects[i].delete()

def clean_rates():
    start = datetime.datetime.strptime('2013-1-1', "%Y-%M-%d").date()
    end = datetime.datetime.strptime('2017-8-9', "%Y-%M-%d").date()
    delta = end - start
    clean_first_rate()
    for i in range(delta.days + 1):
        date = start + datetime.timedelta(days=i)
        try:
            all_objects = Rate.objects.filter(date=date)
            len_o = len(all_objects)
            for i in range(len_o-1):
                all_objects[i].delete()
        except:
            eur_price = Rate.objects.filter(date=date-datetime.timedelta(days=1)).first().eur_price
            gbp_price = Rate.objects.filter(date=date-datetime.timedelta(days=1)).first().gbp_price
            Rate.objects.create(date=date, eur_price=eur_price, gbp_price=gbp_price)

def clean_first_rate():
    date = datetime.datetime.strptime('2013-1-1', "%Y-%M-%d").date()
    all_objects = Rate.objects.filter(date=date)
    len_o = len(all_objects)
    for i in range(len_o-1):
        all_objects[i].delete()
