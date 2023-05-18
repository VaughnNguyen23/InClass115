#Imported class library for tkinter.
import tkinter as tk
from tkinter import ttk

#Create and name event.
def on_select(event):
    
    #create an item object that obtains the value of the selected item.
    selected_item = event.widget.get
    print("Selected item.", selected_item)

#Make the root.
root = tk.Tk()
root.title("Vaughn is funny")

#Created an array of items to place in combobox.
items = ["Item 1","Item 2","Item 3", "Item 4", "Item 5"]
#Create the combo box object, put the object in the root window and populate values.
combo_box = ttk.Combobox(root, values=items)

#The bind function will tie the selected item to the on_selected function.
combo_box.bind("<<ComboboxSelected>>", on_select)

#pack the object to the screen with the geometry manager.
combo_box.pack()

#mainloopp keeps the root parnet window visible
root.mainloop()

