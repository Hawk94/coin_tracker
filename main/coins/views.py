from rest_framework import permissions
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from django.contrib.auth.models import User
from .models import BTC, ETH, LTC

from .serializers import BTCSerializer, ETHSerializer, LTCSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'btc': reverse('btc-list', request=request, format=format),
        'eth': reverse('eth-list', request=request, format=format),
        'ltc': reverse('ltc-list', request=request, format=format)

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
