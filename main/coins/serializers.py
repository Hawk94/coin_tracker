from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BTC, ETH, LTC


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username')


class BTCSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BTC
        fields = ('created', 'price')


class ETHSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ETH
        fields = ('created', 'price')


class LTCSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LTC
        fields = ('created', 'price')