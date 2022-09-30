import tkinter as tk
from newwindow import *

menu = tk.Tk()
menu.title("Furniture Delivery Inc")
menu.configure(bg="lightsteelblue")
width = 700
height = 500
menu.geometry("%dx%d" % (width, height))

for column in range(5):
    menu.columnconfigure(column, weight = 1)

for row in range(6):
    menu.rowconfigure(row, weight = 1)


label = tk.Label(text = "Main Menu", font = ("Arial", 18), bg = "lightsteelblue")
label.grid(column = 2, row = 0)

btn_customer = tk.Button(
    text = "New Customer",
    command = customer
)
btn_customer.grid(column = 2, row = 1)

btn_delivery = tk.Button(
    text="New Delivery"
)
btn_delivery.grid(column = 2, row = 2)

tk.mainloop()