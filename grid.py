from tkinter import *

root = Tk() #Add window

variable1 = Label(root, text="Hello World") #creating label widget
variable2 = Label(root, text="My Name is Kalpit rahtod") #creating label widget
#we can put empty spaces  

variable1.grid(row=0, column=0)
variable2.grid(row=1, column=1)

# we can also do like this 
#variable1 = Label(root, text="Hello World").grid(row=0, column=0)
#variable2 = Label(root, text="My Name is Kalpit rahtod").grid(row=1, column=1)

root.mainloop()
