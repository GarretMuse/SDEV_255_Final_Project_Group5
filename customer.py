from components import *    

def cust_screen():
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

  btn_add = tk.Button(
    window,
    text = "Add",
    command = window.destroy
  )
  btn_add.grid(column = 1, row = 6, sticky = "w")

  btn_delete = tk.Button(
    window,
    text = "Delete",
    command = window.destroy
  )
  btn_delete.grid(column = 2, row = 6, sticky="w")
  
  btn_lookup = tk.Button(
    window,
    text = "Look Up",
    command = window.destroy
  )
  btn_lookup.grid(column = 2, row = 6, sticky="e")

  btn_cancel = tk.Button(
    window,
    text = "Cancel",
    command = window.destroy
  )
  btn_cancel.grid(column = 3, row = 6, sticky="e")