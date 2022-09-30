
class Inventory:


    total_instock = float(input("Enter Instock Items: "))
    total_sold = float(input("Items Sold Today: "))

  
    
    price = 0


    def __init__(self, name, inventory, price):
        self.name = name
        self.inventory = inventory
        self.price = price
       

        Inventory.total_sold += 0
        Inventory.price += 0

    def Total_Inventory(self):
        self.inventory = int(self.total_sold - self.total_instock)
        return '{} {}'.format(self.name, self.inventory, self.price)
    

    def Total_Items_Sold(self):
        self.sold = int(self.total_instock - self.total_sold)
    
    def New_Inventory(self):
        self.instock = int(self.total_instock - self.total_sold)
        return '{} {}'.format(self.name, self.inventory)

  

item1 = Inventory("Couch", "inventory", "price")
item2 = Inventory("Mattress", "inventory", "price")




print(Inventory.New_Inventory(item1))
print(Inventory.Total_Inventory(item1))
