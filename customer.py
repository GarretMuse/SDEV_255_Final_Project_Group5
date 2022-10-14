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

def cust_screen(db):
  window = newWindow("Customer Options")

  title = newLabel(window, "Customer", 16)
  title.grid(column = 2, row = 0,)

  labels = ["Customer #: ", "Name: ", "Phone: ", "Address: ", "Distance: "]
  
  for str in labels:
    label = newLabel(window, str, 12)
    label.grid(column = 0, row = labels.index(str)+1, sticky="e", columnspan=2)
  
  ent_num = tk.Entry(window, width = 40)
  ent_num.grid(column = 2, row = 1, sticky = "w", columnspan=3)

  ent_name = tk.Entry(window, width = 40)
  ent_name.grid(column = 2, row = 2, sticky = "w", columnspan=3)

  ent_phone = tk.Entry(window, width = 40)
  ent_phone.grid(column = 2, row = 3, sticky = "w", columnspan=3)

  ent_addr = tk.Entry(window, width = 40)
  ent_addr.grid(column = 2, row = 4, sticky = "w", columnspan=3)

  ent_dist = tk.Entry(window, width = 40)
  ent_dist.grid(column = 2, row = 5, sticky = "w", columnspan=3)

  fields = (ent_num, ent_name, ent_phone, ent_addr, ent_dist)

  btn_add = tk.Button(
    window,
    text = "Add",
    command = lambda: create_new(db, fields)
  )
  btn_add.grid(column = 1, row = 6, sticky = "w")

  btn_delete = tk.Button(
    window,
    text = "Delete",
    command = lambda: delete(db, fields)
  )
  btn_delete.grid(column = 2, row = 6, sticky="w")
  
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