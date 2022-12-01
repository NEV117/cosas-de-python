# viru 2
import webbrowser
from tkinter import *
from random import randint
import time
import threading

root = Tk()
root.attributes("-alpha", 0)
root.overrideredirect(1)
root.attributes("-topmost", 1)

def browser():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    i = 0
    while True:
        ahegao = "XDXDDDDDDD"
        win = Toplevel(root)
        win.geometry("285x275+" + str(randint(0, root.winfo_screenwidth() - 285)) + "+" + str(randint(0, root.winfo_screenheight() - 275)))
        win.overrideredirect(1)
        Label(win, text= ahegao , fg="black", anchor="e").place(relx=.5, rely=.5, anchor = CENTER)
        win.lift()
        win.attributes("-topmost", True)
        win.attributes("-topmost", False)
        root.lift()
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)
        time.sleep(.05)

        i += 1

threading.Thread(target=browser).start()
root.mainloop()
