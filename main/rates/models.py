from django.db import models
from django.utils import timezone


class Rate(models.Model):
    """A model to record the exchange rate from pounds or euros to dollars on a given date.
    """
    date = models.DateField(default=timezone.now)
    eur_rate = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    gbp_rate = models.DecimalField(max_digits=12, decimal_places=4, default=0)

    class Meta:
        ordering = ('date',)