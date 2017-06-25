from rest_framework import serializers
from .models import Rate


class RateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Rate
        fields = ('date', 'eur_rate', 'gbp_rate')
