from django.conf.urls import url, include
from .views import BTCViewSet, ETHViewSet, LTCViewSet
from main.stocks.views import AAPLViewSet, FBViewSet, GOOGViewSet, NFLXViewSet, MSFTViewSet, AMZNViewSet, SPXViewSet, FANGViewSet, FAMGAViewSet
from main.rates.views import RateViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'btc', BTCViewSet)
router.register(r'eth', ETHViewSet)
router.register(r'ltc', LTCViewSet)
router.register(r'aapl', AAPLViewSet)
router.register(r'fb', FBViewSet)
router.register(r'goog', GOOGViewSet)
router.register(r'nflx', NFLXViewSet)
router.register(r'msft', MSFTViewSet)
router.register(r'amzn', AMZNViewSet)
router.register(r'spx', SPXViewSet)
router.register(r'fang', FANGViewSet)
router.register(r'famga', FAMGAViewSet)
router.register(r'rate', RateViewSet)

schema_view = get_swagger_view(title='Coin Saver: Tracker API')

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
