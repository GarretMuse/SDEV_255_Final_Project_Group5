import tkinter as tk

def newWindow():
  window = tk.Toplevel()
  window.title("Add New Customer")
  window.configure(bg="lightsteelblue")
  width = 700
  height = 500
  window.geometry("%dx%d" % (width, height))
  window.attributes('-topmost', True)

  for column in range(5):
    window.columnconfigure(column, weight = 1)
  for row in range(6):
    window.rowconfigure(row, weight = 1)
  
  return window

def customer():
  window = newWindow()
  label = tk.Label(master = window, text = "New Customer", font = ("Arial", 16), bg = "lightsteelblue")
  label.grid(column = 2, row = 0)

  btn_close = tk.Button(
    window,
    text = "Close",
    command = window.destroy
  )
  btn_close.grid(column = 3, row = 5)

  btn_commit = tk.Button(
    window,
    text = "Close",
    command = window.destroy
  )
  btn_commit.grid(column = 1, row = 5)