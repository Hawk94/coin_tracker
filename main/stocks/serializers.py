from rest_framework import serializers
from .models import AAPL, FB, GOOG, NFLX, FANG


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


class FANGSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FANG
        fields = ('date', 'price')
