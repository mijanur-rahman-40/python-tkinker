from Tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
root = Tk()
root.title('Simple graph implementation')
# root.iconbitmap('./index.ico')
root.geometry('400x200')


def graph():
    housePrices = np.random.normal(200000, 25000, 5000)
    plt.hist(housePrices, 200)
    plt.show()


myButton = Button(root, text='Graph it', command=graph)
myButton.pack()

root.mainloop()
