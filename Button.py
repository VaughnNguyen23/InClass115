#imports class library (class tkinter)
import tkinter as tk

#Prints buttun clicked
def button_click():
    print("Button Clicked")

#Building the root 
root = tk.Tk()
root.title("Button Example")

#Heres our button. Button pack is for the geometry of the button
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

#This is what keeps the window open for function
root.mainloop()


