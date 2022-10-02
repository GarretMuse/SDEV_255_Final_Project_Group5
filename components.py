import tkinter as tk

def newLabel(window, str, size):
  label = tk.Label(window, text = str, font = ("Arial", size), bg = "lightsteelblue")
  return label

def newWindow(name):
  window = tk.Toplevel()
  window.title(name)
  window.configure(bg="lightsteelblue")
  width = 700
  height = 500
  window.geometry("%dx%d" % (width, height))
  window.attributes('-topmost', True)

  for column in range(5):
    window.columnconfigure(column, weight = 1)
  for row in range(7):
    window.rowconfigure(row, weight = 1)
    
    #these frames are just to help me see the layout and this section will be deleted
    #for col in range(5):
     # for r in range(7):
      # frame = tk.Frame(window, bg = "red")
       #frame.grid(column =col, row = r, sticky = "nsew", padx = 1, pady = 1)

  return window