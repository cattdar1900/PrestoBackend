from django.db import models

from datetime import *

STATES = (
    ('0' , 'off'),
    ('1' , 'on')
)

typeMenu = (
    ('Onedis','อาหารจารเดียว'),
    ('non-Onedis','กับข้าว')

)

foodtype = (
    ('food','อาหาร'),
    ('drink','เครื่องดื่ม'),
    ('snack','ของทานเล่น'),
    ('bakery','ของหวาน')
)
payment = (
    ('online','โอน'),
    ('clash','เงินสด'),
    ('online + clash','โอน + เงินสด')
)
foodEX = (
    ('normal','ธรรมดา'),
    ('extra','พิเศษ')
)
typeDrink = (
    ('hot','ร้อน'),
    ('cool','เย็น'),
    ('spin','ปั่น')
)

class CallService(models.Model):
    name = models.CharField(max_length= 50)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50,choices = STATES)
    def __str__(self):
        return self.name 



class Rider(models.Model):
    name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    def __str__(self):
        return self.name 
    
class StateRider(models.Model):
    takeOrder = models.BooleanField(default=False)
    timeTakeOrder = models.DateTimeField(default=datetime.now(),null=True, blank=True)
    takeFood = models.BooleanField(default = False)
    timeTakeFood = models.DateTimeField(default=datetime.now(),null=True, blank=True)
    finishOrder = models.BooleanField(default = False)
    timeFinishOrder = models.DateTimeField(default=datetime.now(),null=True, blank=True)



class Market(models.Model):
    
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    timeToOpen = models.TimeField(blank=True)
    timeToClose = models.TimeField(blank = True)
    def __str__(self):
        return self.name



class Option(models.Model):
    name = models.CharField(max_length = 20)
    price = models.PositiveIntegerField()
    typefoods = models.CharField(max_length = 10,choices = foodtype)
    markets = models.ForeignKey(Market,null = True, on_delete = models.SET_NULL)
    def __str__(self):
        return self.typefoods + " " + self.name




class Order(models.Model):
    customer = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    phoneNumber = models.CharField(max_length = 20)
    timeToSend = models.DateTimeField(default=datetime.now(),null=True, blank=True)
    timeToOrder = models.DateTimeField(default=datetime.now(),null=True, blank=True)
    totalPriceOrder = models.PositiveIntegerField()
    payments = models.CharField(max_length = 50, choices = payment)
    callService = models.ForeignKey(CallService,null = True , on_delete = models.SET_NULL)
    

    def __str__(self):
        return self.customer +" ส่งที่ "+ self.address
class Food(models.Model):
    name = models.CharField(max_length = 50)
    exFood = models.CharField(max_length = 20,choices = foodEX)
    priceBase = models.PositiveIntegerField()
    markets = models.ForeignKey(Market,null = True,on_delete = models.SET_NULL)
    def __str__(self):
         return self.name + " " + (str)(self.priceBase) + " " + self.exFood + " " + self.markets.name

class Drink(models.Model):
    name = models.CharField(max_length = 20)
    typeDrinks =models.CharField(max_length = 20,choices = typeDrink)
    priceBase = models.PositiveIntegerField()
    markets = models.ForeignKey(Market,null = True,on_delete = models.SET_NULL)
    def __str__(self):
        return self.name + " " + (str)(self.priceBase) + " " + self.typeDrinks + " " + self.markets.name

class Snack(models.Model):
    name = models.CharField(max_length = 20)
    exFood = models.CharField(max_length = 20,choices = foodEX)
    priceBase = models.PositiveIntegerField()
    markets = models.ForeignKey(Market,null = True,on_delete = models.SET_NULL)
    def __str__(self):
         return self.name + " " + (str)(self.priceBase) + " " + self.exFood + " " + self.markets.name

class OnMenu(models.Model):
    foods = models.ForeignKey(Food,null =True,blank=True,on_delete = models.CASCADE)
    drink = models.ForeignKey(Drink,null =True,blank=True,on_delete = models.CASCADE)
    snack = models.ForeignKey(Snack,null =True,blank=True,on_delete = models.CASCADE)

class Menu(models.Model):
    amount = models.PositiveIntegerField()
    onMenu = models.OneToOneField(OnMenu,on_delete = models.CASCADE)
    market = models.ForeignKey(Market,null = True,on_delete = models.SET_NULL)
    order = models.ForeignKey(Order,null = True,on_delete = models.SET_NULL)
    totalPriceMenu = models.PositiveIntegerField()
    def __str__(self):
        return self.market.name +" "+ self.onMenu.foods.name + " จำนวน " + (str)(self.amount) + " ราคา " + (str)(self.totalPriceMenu)

class FoodOption(models.Model):
    option = models.ForeignKey(Option,null = True,on_delete=models.SET_NULL)
    menu = models.ForeignKey(Menu,null = True,on_delete = models.SET_NULL)
    amout = models.PositiveIntegerField()
    def __str__(self):
        return self.option.name + " " + (str)(self.option.price) + " บาท "

class StatusOrder(models.Model):
    #OneToOne
    rider = models.OneToOneField(Rider,on_delete = models.CASCADE)
    #OneToOne 
    staterider = models.OneToOneField(StateRider,on_delete = models.CASCADE)
    order = models.OneToOneField(Order,on_delete = models.CASCADE)

    def __str__(self):
        return self.rider.name + " รับออเดอร์ของ " + self.order.customer 


     



    



