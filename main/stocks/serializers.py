from rest_framework import serializers
from .models import AAPL, FB, GOOG, NFLX, MSFT, AMZN, SPX, FANG, FAMGA


class AAPLSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AAPL
        fields = ('date', 'price')


class FBSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FB
        fields = ('date', 'price')


class GOOGSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GOOG
        fields = ('date', 'price')


class NFLXSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NFLX
        fields = ('date', 'price')


class AMZNSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AMZN
        fields = ('date', 'price')


class MSFTSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MSFT
        fields = ('date', 'price')


class SPXSerializer(serializers.HyperlinkedModelSerializer):
    """
    S&P 500
    """

    class Meta:
        model = SPX
        fields = ('date', 'price')


class FANGSerializer(serializers.HyperlinkedModelSerializer):
    """
    Facebook, Amazon, Netflix, Google.
    """

    class Meta:
        model = FANG
        fields = ('date', 'price')


class FAMGASerializer(serializers.HyperlinkedModelSerializer):
    """
    Facebook, Amazon, Microsoft, Google, Apple
    """

    class Meta:
        model = FAMGA
        fields = ('date', 'price')

