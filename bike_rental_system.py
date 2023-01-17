class bikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displaystock(self):
        print("Total Bikes Available",self.stock)

    def rentforBike(self,q):

        if q<=0:
            print("Enter the positive value or greater then zero")

        elif q>self.stock:
            print("Enter the value(less then stock")

        else:
            self.stock=self.stock-q
            print("Total Prices",q*100)
            print("Total Bikes",self.stock)



    while True:
        obj=bikeShop(100)
        userchoice=int(input('''
        1.Display stocks
        2.Rent a bike
        3.Exit'''))

        if userchoice==1:
                obj.displaystock()

        elif userchoice==2:
                n=int(input("Enter the qty:----"))
                obj.rentforBike()

        else:
                break



