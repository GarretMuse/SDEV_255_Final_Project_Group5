
from inventory import Inventory

class Profit(Inventory):
    total_price = float(input("Final Sale Price: "))

    total_sold = float(input("Total Items Sold: "))


    def __init__(self, name, profit):
        self.name = name
        self.profit = profit


        Profit.total_price += .0


    def Weekly_Profit(self):
        self.profit = (self.total_price * self.total_sold)
        if self.profit >= 1:
            return '{} {}'.format(self.name, self.profit)
        elif self.profit <=1:
            return self.profit
        else:
            quit()

        

    


week1 = Profit("First week", "profit")
week2 = Profit("Second week", "profit")




print(Profit.Weekly_Profit(week1))

