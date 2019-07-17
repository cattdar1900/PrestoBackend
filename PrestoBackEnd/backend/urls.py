from django.urls import path , include
from django.conf.urls import url
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from .views import *

router = routers.DefaultRouter()
router.register(r'callservice',CallServiceViewSet)

v = 9999

urlpatterns = [
    url(r'^auth/',ObtainAuthToken.as_view()),
    url(r'^foods',FoodViewSetByFoodname.as_view(),name='Food-list'),
    url(r'^food',FoodViewSetByMarketName.as_view(),name='food-list-market'),
    url(r'^callservices/(?P<id>\w+)$',CallServiceViewSet.as_view(),name='callservice-list'),
    url(r'^callservices',CallServiceByDetail.as_view({'get':'list'})),
    url(r'^markets',MarketAPIView.as_view())
    
    # url(r'^',include(router.urls))
]
    