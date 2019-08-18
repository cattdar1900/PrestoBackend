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
#API find market by foodname
class MarketAPIView(generics.ListAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('food__name',)

#list market
class MarketApiViewByMarket(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

#Create On menu
class OnMenuCreate(generics.ListCreateAPIView):
    queryset =  OnMenu.objects.all()
    serializer_class = OnMenuSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=randomkey',)
    
#API find Option by Markets
class OptionByMarkets(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('markets__name',)

#Create Food OP
class FoodOptionCreate(generics.ListCreateAPIView):
    queryset =  FoodOption.objects.all()
    serializer_class = FoodOptionSerailizer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=randomkey',)

class OrderCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerailizer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id',)
    
class MenuCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerailizer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id',)

class DrinkBymarket(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('markets__name',)

class SnackBymarket(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('markets__name',)


# Create your views here.
