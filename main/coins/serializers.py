from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BTC, ETH


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')


class BTC(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BTC
        fields = ('url', 'id', 'owner', 'period', 'period_open', 'period_close', 'period_high', 'period_low',
                  'duration')


class ETH(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ETH
        fields = ('url', 'id', 'owner', 'period', 'period_open', 'period_close', 'period_high', 'period_low',
                  'duration')
