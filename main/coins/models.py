from django.db import models
from ..exchanges.models import Exchange


class BaseCoin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    period = models.DurationField()
    period_open = models.DecimalField(decimal_places=8)
    period_close = models.DecimalField(decimal_places=8)
    period_high = models.DecimalField(decimal_places=8)
    period_low = models.DecimalField(decimal_places=8)
    period_volume = models.DecimalField(decimal_places=8)

    class Meta:
        abstract = True
        ordering = ('created',)


class BTC(BaseCoin):


class ETH(BaseCoin):
