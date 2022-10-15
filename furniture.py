from components import *
from database import *

class Furniture:
  id = 0 
  def __init__(self, desc, price, stock):
    self.desc = desc
    self.price = price
    self.stock = stock

def create_new(db, fields):
  furn = Furniture(fields[1].get(), fields[2].get(), fields[3].get())
  db.insert(furn)

def delete(db, fields):
  furn = Furniture(fields[1].get(), fields[2].get(), fields[3].get())
  furn.id = fields[0].get()
  db.remove(furn)
  clear(fields)

def look_up(db, fields):
  data = db.fetch("Furniture", fields[0].get(), fields[2].get())
  clear(fields)
  for i in range(len(fields)):
    fields[i].insert(0, data[i])
  
def clear(fields):
  for field in fields:
    field.delete(0, tk.END)

def modify(db, fields):
  furn = Furniture(fields[1].get(), fields[2].get(), fields[3].get())
  furn.id = fields[0].get()
  db.update(furn)



def furn_screen(db):
  window = newWindow("Furniture Options")

  title = newLabel(window, "Furniture", 16)
  title.grid(column = 2, row = 0,)

  labels = ["Item #: ", "Description: ", "Price: ", "In Stock: "]
  fields = []
  
  for str in labels:
    label = newLabel(window, str, 12)
    label.grid(column = 1, row = labels.index(str)+1)
    entry = tk.Entry(window, width = 40)
    fields.append(entry)
    entry.grid(column = 2, row = labels.index(str)+1, sticky="w", columnspan=3)

  btn_names = ["Search", "Add", "Delete", "Update", "Clear", "Cancel"]
  buttons = []

  for str in btn_names:
    button = newButton(window, str)
    button.grid(column = 0, row = btn_names.index(str)+1, sticky = "n")
    buttons.append(button)

  buttons[0].configure(command = lambda: look_up(db, fields))  
  buttons[1].configure(command = lambda: create_new(db, fields))
  buttons[2].configure(command = lambda: delete(db, fields))
  buttons[3].configure(command = lambda: modify(db, fields))
  buttons[4].configure(command = lambda: clear(fields))
  buttons[5].configure(command = window.destroy)