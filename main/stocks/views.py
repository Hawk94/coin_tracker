from rest_framework import viewsets

from .models import AAPL, FB, GOOG, NFLX, MSFT, AMZN, SPX, FANG, FAMGA

from .serializers import AAPLSerializer, FBSerializer, GOOGSerializer, NFLXSerializer, MSFTSerializer, AMZNSerializer, SPXSerializer, FANGSerializer, FAMGASerializer


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


class MSFTViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MSFT.objects.all()
    serializer_class = MSFTSerializer


class AMZNViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = AMZN.objects.all()
    serializer_class = AMZNSerializer


class SPXViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = SPX.objects.all()
    serializer_class = SPXSerializer


class FANGViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = FANG.objects.all()
    serializer_class = FANGSerializer


class FAMGAViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = FAMGA.objects.all()
    serializer_class = FAMGASerializer
