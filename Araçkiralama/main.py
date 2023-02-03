from rent import BikeRent,CarRent,Customer

bike=BikeRent(100)
car = CarRent(10)
customer = Customer()
main_menu= True

while True:
    if main_menu:
        print("""******** Vehicle Rental Shop ********
        A.Bike menu
        B.Car menu
        C.Exit
        """)
        main_menu = False
        choice = input("enter choice :  ")
    if choice == 'A':
        print(""" ********** Bike Menu **********
        1.Display available bikes
        2.Request a bike hourl basis $ 5
        3.Request a bike daily basis $ 84
        4.Return a bike
        5.Main menu
        6.Exit 
        """)
        choice = input("enter choice :")
        try:
            choice = int(choice)
        except ValueError:
            print("it is not ınteger")
            continue
        if choice == 1:
            bike.displaystock()
            choice == "A"
        elif choice == 2:
            customer.rentalTime_b = bike.rentHpourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("-----------------------------------------------")
        elif choice == 3:
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("-----------------------------------------------------")
        elif choice == 4:
            customer.bill= bike.returnVehicle(customer.returnVehicle("bike"),"bike")
            customer.rentalBasis_b,customer.rentalTime_b,customer.bikes = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("invalid input return between 1 and 6")
            main_menu = True

    elif choice == 'B':
        print(""" ********** Cars Menu **********
        1.Display available cars
        2.Request a car hourl basis $ 10
        3.Request a car daily basis $ 192
        4.Return a car
        5.Main menu
        6.Exit 
        """)
        try:
            choice = int(choice)
        except ValueError:
            print("it is not ınteger")
            continue
        if choice == 1:
            bike.displaystock()
            choice == 'B'
        elif choice == 2:
            customer.rentalTime_c = car.rentHpourly(customer.requestVehicle("car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("-----------------------------------------------")
        elif choice == 3:
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("-----------------------------------------------------")
        elif choice == 4:
            customer.bill = car.returnVehicle(customer.returnVehicle("car"), "car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0, 0, 0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("invalid input return between 1-6")
            main_menu = True

    elif choice == 'Q':
        break
    else:
        print("invalid input please enter A-B-Q")
        main_menu = True
    print("Bizi tercih ettiginiz için teşekkür ederiz")









