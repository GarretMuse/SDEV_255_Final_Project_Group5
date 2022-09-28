
class Inventory:
    instock = 0
    sold = 0
   
    total_sold = float(input("Enter Items Sold Today: "))
    total_instock = float(input("Enter Instock Items: "))


    def __init__(self, name, inventory, price):
        self.name = name
        self.inventory = inventory
        self.price = price


        Inventory.instock +=1


    def Total_Inventory(self):
        return '{} {}'.format(self.name, self.instock)
    

    def Total_Items_Sold(self):
        self.sold = int(self.sold - self.Total_Inventory)
    
    def New_Inventory(self):
        self.instock = int(self.instock - self.sold)


item1 = Inventory("Couch", "inventory", "price")
item2 = Inventory("Mattress", "inventory", "price")




print(Inventory.Total_Inventory(item1))
