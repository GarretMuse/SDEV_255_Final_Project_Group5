
from inventory import Inventory

class Profit(Inventory):
    total_price = float(input("enter Price of item:"))
    total_sold = float(input("Enter Amount Sold:"))


    def __init__(self, name, profit):
        self.name = name
        self.profit = profit


        Profit.total_price += .0


    def Weekly_Profit(self):
        self.profit = (self.total_price * self.total_sold)
        return '{} {}'.format(self.name, self.profit)

    


week1 = Profit("First week", "profit")
week2 = Profit("Second week", "profit")




print(Profit.Weekly_Profit(week1))
