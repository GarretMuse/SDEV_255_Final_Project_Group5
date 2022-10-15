from database import *
from components import *
   

class Order:
  id = 0 
  

def create_new(db, fields):
  pass

def delete(db, fields):
  pass

def look_up(db, fields):
  pass
  
def clear(fields):
  for field in fields:
    field.delete(0, tk.END)

def ord_screen(db):
    window = newWindow("Order Options")

    #these frames are just to help me see the layout and this section will be deleted
    #for col in range(5):
    #    for r in range(6):
    #        frame = tk.Frame(window, bg = "red")
    #        frame.grid(column =col, row = r, sticky = "nsew", padx = 1, pady = 1)
    
    title = newLabel(window, "Orders", 16)
    title.grid(column = 2, row = 0,)

    ord_text = tk.Text(window, width = 1, height = 1)
    ord_text.grid(column = 3, row = 1, sticky = "nsew", columnspan = 2, rowspan = 4, padx = 10, pady=5)