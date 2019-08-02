from rest_framework import serializers
from .models import CallService,Rider,StateRider,StatusOrder,Menu,Market,FoodOption,Option,Order,Food,Drink,Snack,OnMenu

class CallServiceSerializer(serializers.ModelSerializer):
    class Meta :
        model = CallService
        fields = ('id','name','username','password','status')
        extra_kwargs = {'password' : {'write_only': True , 'required':True}}
        def create(self, validated_data):
            user = CallService.objects.create_user(**validated_data)
            user.save()
            return user
        

class RiderSerializer(serializers.ModelSerializer):
    class Meta :
        model = Rider
        fields = ('id','name','username','password')
        extra_kwargs = {'password' : {'write_only': True , 'required':True}}
    

class StatusRiderSerializer(serializers.ModelSerializer):
    class Meta : 
        model = StateRider
        fields = ('id','takeOrder','timeTakeOrder','takeFood','timeTakeFood','finishOrder','timeFinishOrder')

class StatusOrderSerializer(serializers.ModelSerializer):
    rider = RiderSerializer(read_only = True)
    statusRider = StatusRiderSerializer(read_only = True)
    class Meta :
        model = StatusOrder
        fields = ('id','rider','statusRider') 

class FoodSerializer(serializers.ModelSerializer):
    class Meta :
        model = Food
        fields = ('id','name','exFood','priceBase','markets')

class MarketSerializer(serializers.ModelSerializer):
    food = FoodSerializer(many=True, read_only=True)
    class Meta :
        model = Market
        fields = ('id','name','location','timeToOpen','timeToClose','food')

class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = ("name","exFood","priceBase","markets")

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ("name","typeDrinks","priceBase","markets")

class OnMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnMenu
        fields = ("foods","drink","snack","randomkey")
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ("name","price","typefoods","markets")

class FoodOptionSerailizer(serializers.ModelSerializer):
    class Meta:
        model = FoodOption
        fields = ("option","amout","randomkey")
