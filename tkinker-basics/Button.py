from Tkinter import *

# here root basically a widget
root = Tk()

def myClick():
    myLabel = Label(root, text='Look I clicked a Button')
    myLabel.pack()

# create a button 
# myButton = Button(root, text='Click me', state=DISABLED)
myButton = Button(root, text='Click me', command=myClick,fg='white', bg='blue')
myButton.pack()

# always looping into window
root.mainloop()
