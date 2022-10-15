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
    label.grid(column = 0, row = labels.index(str)+1, sticky="e", columnspan=2)
    entry = tk.Entry(window, width = 40)
    fields.append(entry)
    entry.grid(column = 2, row = labels.index(str)+1, sticky="w", columnspan=3)

  btn_update = tk.Button(
    window,
    text = "Update",
    command = lambda: modify(db, fields)
  )
  btn_update.grid(column = 3, row = 4)

  btn_stock = tk.Button(
    window,
    text = "Add",
    command = lambda: create_new(db, fields)
  )
  btn_stock.grid(column = 1, row = 6, sticky = "w")

  btn_add = tk.Button(
    window,
    text = "Delete",
    command = lambda: delete(db, fields)
  )
  btn_add.grid(column = 2, row = 6, sticky="w")
  
  btn_lookup = tk.Button(
    window,
    text = "Look Up",
    command = lambda: look_up(db, fields)
  )
  btn_lookup.grid(column = 2, row = 6, sticky="e")

  btn_cancel = tk.Button(
    window,
    text = "Clear",
    command = lambda: clear(fields)
  )
  btn_cancel.grid(column = 3, row = 6, sticky="e")