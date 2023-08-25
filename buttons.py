from tkinter import *

root = Tk() #Add window

def myClick():
    myLabel = Label(root, text="Look! I clicked button")
    myLabel.pack()

myButton = Button(root, text="ReadMe", command=myClick) #state=DISABLED padx=50(Inner space) pady=50 -myClick(), Automatically run it fg="blue" bg="red" u can use hec colour code
myButton.pack()

root.mainloop()
