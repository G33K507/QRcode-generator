try:
    from tkinter import *
except ImportError:
    from Tkinter import *

import pyqrcode
import png

mainWin = Tk()
mainWin.title('QRcodeGen')
mainWin.minsize(300,100)
mainWin.configure(background="darkslategray")

def qcode():
    string = enter.get()
    img = pyqrcode.create(string)
    img.show(img)

label1 = Label(mainWin, text="--Input--", fg="aquamarine", bg="darkslategray")
label1.pack()

enter = Entry(mainWin)
enter.pack()

btn1 = Button(mainWin,text='Generate!',command=qcode, bg="gray")
btn1.pack(side='top')

mainWin.mainloop()
