from Tkinter import *

# here root basically a widget
root = Tk()
# create a label as a widget
myLabel1 = Label(root, text='Hello world')
myLabel2 = Label(root, text='My name is mijanur rahman')
myLabel3 = Label(root, text='')
# showing it onto screen
# myLabel.pack()

# Positioning gris system
# grid system position basically use relative position
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)
# myLabel3.grid(row=2, column=1)

# always looping into window
root.mainloop()
