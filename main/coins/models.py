from django.db import models
from datetime import timedelta


class BaseCoin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    exchange = models.CharField(max_length=100, blank=True, default='')
    price = models.DecimalField(max_digits=12, decimal_places=4, default=0)

    class Meta:
        abstract = True
        ordering = ('created',)


class BTC(BaseCoin):
    market_cap = models.DecimalField(max_digits=18, decimal_places=8, default=0)


class ETH(BaseCoin):
    market_cap = models.DecimalField(max_digits=18, decimal_places=8, default=0)


class LTC(BaseCoin):
    market_cap = models.DecimalField(max_digits=18, decimal_places=8, default=0)
