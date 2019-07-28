from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated ,AllowAny
from .models import *
from rest_framework import generics,viewsets,filters
from .Serializers import *



# API for search by id 
class CallServiceViewSet(generics.ListCreateAPIView):
    queryset = CallService.objects.all()
    serializer_class = CallServiceSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get_queryset(self):
        queryset = CallService.objects.filter(pk=self.kwargs['id'])
        return queryset

# API for show list  
class CallServiceByDetail(viewsets.ModelViewSet):
    queryset = CallService.objects.all()
    serializer_class = CallServiceSerializer

class FoodViewSetByFoodname(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','markets__name',)

# API for find food by market
class FoodViewSetByMarketName(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('markets__name',)

class MarketAPIView(generics.ListAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('food__name',)

class MarketApiViewByMarket(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    

# Create your views here.
