from Tkinter import *
import ttk

root = Tk()
root.title('Dropdown menu with tkinter')
root.geometry('600x600')

options = [
    'Monday', 'Wednesday', 'Thursday', 'Friday'
]
# drop down boxes
clicked = StringVar()
clicked.set(options[0])


def selected(event):
    # myLabel = Label(root, text=clicked.get()).pack()
    if clicked.get() == 'Friday':
        myLabel = Label(root, text="Yay! It's Friday").pack()
    else:
        myLabel = Label(root, text=clicked.get()).pack()


def comboboxClick(event):
    if myCombo.get() == 'Friday':
        myLabel = Label(root, text="Yay! It's Friday").pack()
    else:
        myLabel = Label(root, text=myCombo.get()).pack()


drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboboxClick)
myCombo.pack()

root.mainloop()
