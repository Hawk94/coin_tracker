from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User
from .models import BTC, ETH, LTC

from .serializers import BTCSerializer, ETHSerializer, LTCSerializer, UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'btc': reverse('btc-list', request=request, format=format),
        'eth': reverse('eth-list', request=request, format=format),
        'ltc': reverse('ltc-list', request=request, format=format),
        'aapl': reverse('aapl-list', request=request, format=format),
        'fb': reverse('fb-list', request=request, format=format),
        'goog': reverse('goog-list', request=request, format=format),
        'msft': reverse('msft-list', request=request, format=format),
        'amzn': reverse('amzn-list', request=request, format=format),
        'fang': reverse('fang-list', request=request, format=format),
        'famga': reverse('famga-list', request=request, format=format)

    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BTCViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = BTC.objects.all()
    serializer_class = BTCSerializer


class ETHViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ETH.objects.all()
    serializer_class = ETHSerializer


class LTCViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = LTC.objects.all()
    serializer_class = LTCSerializer
