from rest_framework import viewsets

from .models import AAPL, FB, GOOG, NFLX, FANG

from .serializers import AAPLSerializer, FBSerializer, GOOGSerializer, NFLXSerializer, FANGSerializer


class AAPLViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = AAPL.objects.all()
    serializer_class = AAPLSerializer


class GOOGViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = GOOG.objects.all()
    serializer_class = GOOGSerializer


class FBViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = FB.objects.all()
    serializer_class = FBSerializer


class NFLXViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = NFLX.objects.all()
    serializer_class = NFLXSerializer


class FANGViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = FANG.objects.all()
    serializer_class = FANGSerializer
