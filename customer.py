from turtle import update
from database import *
from components import *
   

class Customer:
  id = 0 
  def __init__(self, name, phone, addr, dist):
    self.name = name
    self.phone = phone
    self.addr = addr
    self.dist = dist

def create_new(db, fields):
  cust = Customer(fields[1].get(), fields[2].get(), fields[3].get(), fields[4].get())
  db.insert(cust)

def delete(db, fields):
  cust = Customer(fields[1].get(), fields[2].get(), fields[3].get(), fields[4].get())
  cust.id = fields[0].get()
  db.remove(cust)
  clear(fields)

def look_up(db, fields):
  data = db.fetch("Customers", fields[0].get(), fields[2].get())
  clear(fields)
  for i in range(len(fields)):
    fields[i].insert(0, data[i])
  
def clear(fields):
  for field in fields:
    field.delete(0, tk.END)

def modify(db, fields):
  cust = Customer(fields[1].get(), fields[2].get(), fields[3].get(), fields[4].get())
  cust.id = fields[0].get()
  db.update(cust)

def cust_screen(db):
  window = newWindow("Customer Options")
  
  title = newLabel(window, "Customer", 16)
  title.grid(column = 2, row = 0,)

  labels = ["Customer #: ", "Name: ", "Phone: ", "Address: ", "Distance: "]
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