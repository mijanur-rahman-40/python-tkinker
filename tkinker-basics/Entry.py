from Tkinter import *

# here root basically a widget
root = Tk()

entry = Entry(root, width=50, borderwidth=2)
entry.pack()
entry.insert(0, 'Enter your name: ')

def myClick():
    myLabel = Label(root, text='Hello ' + entry.get())
    myLabel.pack()

myButton = Button(root, text='Enter your name', command=myClick,fg='white', bg='blue')
myButton.pack()

# always looping into window
root.mainloop()
