from django.db import models
from django.utils import timezone


class BaseStock(models.Model):
    date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=12, decimal_places=4, default=0)

    class Meta:
        abstract = True
        ordering = ('date',)


class AAPL(BaseStock):
    market_cap = models.DecimalField(max_digits=18, decimal_places=8, default=0)


class FB(BaseStock):
    market_cap = models.DecimalField(max_digits=18, decimal_places=8, default=0)


class GOOG(BaseStock):
    market_cap = models.DecimalField(max_digits=18, decimal_places=8, default=0)


class NFLX(BaseStock):
    market_cap = models.DecimalField(max_digits=18, decimal_places=8, default=0)


class FANG(BaseStock):
    market_cap = models.DecimalField(max_digits=18, decimal_places=8, default=0)
