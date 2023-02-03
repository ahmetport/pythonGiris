#Parent class
import datetime
class VehicleRent():
    def __init__(self,stock):
        self.stock= stock
        self.now = 0

    def displaystock(self):
        print("{} vehicle to available to rent".format(self.stock))
        return self.stock


    def rentHpourly(self,n):
        if n <= 0 :
            print("number should be positive")
            return None
        elif n > self.stock:
            print("sorry, {} vehicle to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("rented a {} vehicle for hourly".format(n,self.now.hour))
            self.stock -= n
            return self.now



    def rentDaily(self,n):
        if n <= 0:
            print("number should be positive")
            return None
        elif n > self.stock:
            print("sorry, {} vehicle to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("rented a {} vehicle for hourly".format(n, self.now.hour))
            self.stock -= n
            return self.now


    def returnVehicle(self,request,brand):
        car_h_price=10
        car_d_price=car_h_price*8/10*24
        bike_h_price=5
        bike_d_price=bike_h_price*7/10*24

        rentaTime,rentalBasis,numofVehicle=request
        bill = 0
        if brand == "car":
            if rentaTime and rentalBasis and numofVehicle :
                self.stock += numofVehicle
                now = datetime.datetime.now()
                rentalPeriod=now - rentaTime

                if rentalBasis == 1: # hourly
                    bill = rentalPeriod.seconds/3600*car_h_price*numofVehicle
                elif rentalBasis == 2: # daily
                    bill=rentalPeriod.seconds/(3600*24)*car_d_price*numofVehicle
                if 2 <= numofVehicle:
                    print("you have extra %20 discount")
                    bill = bill*0.8
                print("thank you for returnning your car")
                print("price {}".format(bill))
                return bill
        elif brand == "bike":
            if rentaTime and rentalBasis and numofVehicle:
                self.stock += numofVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentaTime

                if rentalBasis == 1:  # hourly
                    bill = rentalPeriod.seconds / 3600 * bike_h_price * numofVehicle
                elif rentalBasis == 2:  # daily
                    bill = rentalPeriod.seconds / (3600 * 24) * bike_d_price * numofVehicle
                if 2 <= numofVehicle:
                    print("you have extra %20 discount")
                    bill = bill * 0.8
                print("thank you for returnning your bike")
                print("price {}".format(bill))
                return bill
        else:
            print("you do not rent a vehicle")
            return None


#child class
class CarRent(VehicleRent):
    global discount_rate # global bi tane rate ekledim
    discount_rate = 15
    def __init__(self,stock):
        super().__init__(stock) # parent classımızdan inherite ettik
    def discount(self,b):
        bill= b-(b*discount_rate)/100
        return bill


#child class1
class BikeRent(VehicleRent):
    def __init__(self,stock):
        super().__init__(stock)

#Customerr
class Customer:
    def __init__(self):
        self.bikes=0
        self.rentalBasis_b =0
        self.rentalTime_b=0

        self.cars=0
        self.rentalBasis_c=0
        self.rentalTime_c=0

    def requestVehicle(self,brand):
        if brand == "bike":
            bikes = input("how many bikes would you like to rent")
            try:
                bikes=int(bikes)
            except ValueError:
                print("number should be number")
                return  -1
            if bikes < 1 :
                print("not umber of bikes should be greater than zero" )
                return -1
            else:
                self.bikes = bikes
            return self.bikes

        elif brand == "car":
            cars = input("how many cars would you like to rent")
            try:
                cars=int(cars)
            except ValueError:
                print("number should be number")
                return  -1
            if cars < 1 :
                print("not umber of cars should be greater than zero" )
                return -1
            else:
                self.cars = cars
            return self.cars


    def returnVehicle(self,brand):
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0,0,0

        else:
            print("return vehicle error")
















