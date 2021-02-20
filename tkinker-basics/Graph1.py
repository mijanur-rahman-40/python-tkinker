from Tkinter import *
import numpy as np

# this helps matplotlib into embedded with tkinter 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = Tk()
root.wm_title('Embedding in Tk')

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, 0.01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# drawing area
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

def on_key_press(event):
    print("You pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('Key_press_event', on_key_press)

def quit():
    root.quit()
    root.destroy()

button = Button(master=root, text='Quit', command=quit)
button.pack(side=BOTTOM)
root.mainloop()