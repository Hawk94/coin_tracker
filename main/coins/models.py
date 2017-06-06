from django.db import models
from django.utils import timezone


class BaseCoin(models.Model):
    date = models.DateField(default=timezone.now)
    exchange = models.CharField(max_length=100, blank=True, default='')
    price = models.DecimalField(max_digits=12, decimal_places=4, default=0)

    class Meta:
        abstract = True
        ordering = ('date',)


class BTC(BaseCoin):
    market_cap = models.DecimalField(max_digits=18, decimal_places=8, default=0)


class ETH(BaseCoin):
    market_cap = models.DecimalField(max_digits=18, decimal_places=8, default=0)


class LTC(BaseCoin):
    market_cap = models.DecimalField(max_digits=18, decimal_places=8, default=0)
