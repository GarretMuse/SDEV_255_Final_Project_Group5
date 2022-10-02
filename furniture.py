from components import *    

def furn_screen():
  window = newWindow("Furniture Options")

  title = newLabel(window, "Furniture", 16)
  title.grid(column = 2, row = 0,)

  labels = ["Item #: ", "Description: ", "Price: ", "In Stock: "]
  
  for str in labels:
    label = newLabel(window, str, 12)
    label.grid(column = 0, row = labels.index(str)+1, sticky="e", columnspan=2)
  
  ent_num = tk.Entry(window, width = 40)
  ent_num.grid(column = 2, row = 1, sticky = "w", columnspan=3)

  ent_desc = tk.Entry(window, width = 40)
  ent_desc.grid(column = 2, row = 2, sticky = "w", columnspan=3)

  ent_price = tk.Entry(window, width = 40)
  ent_price.grid(column = 2, row = 3, sticky = "w", columnspan=3)

  ent_stock = tk.Entry(window, width = 40)
  ent_stock.grid(column = 2, row = 4, sticky = "w", columnspan=3)

  btn_stock = tk.Button(
    window,
    text = "Change Stock",
    command = window.destroy
  )
  btn_stock.grid(column = 1, row = 6, sticky = "w")

  btn_add = tk.Button(
    window,
    text = "Add",
    command = window.destroy
  )
  btn_add.grid(column = 2, row = 6, sticky="w")
  
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