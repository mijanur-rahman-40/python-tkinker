from Tkinter import *

root = Tk()
root.title('Dropdown menu with tkinter')
root.geometry('600x600')

options = [
     'Monday', 'Wednesday', 'Thursday', 'Friday'
]
# drop down boxes
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

def show():
    myLabel = Label(root, text=clicked.get()).pack()
    
myButton = Button(root, text='Show Selection',command=show).pack()

root.mainloop()