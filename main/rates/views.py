from rest_framework import viewsets

from .models import Rate

from .serializers import RateSerializer


class RateViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Rate.objects.all()
    serializer_class = RateSerializer