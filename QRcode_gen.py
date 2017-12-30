from Tkinter import *
import pyqrcode
import png

mainWin = Tk()

mainWin.minsize(300,100)

label1 = Label(mainWin, text="--Input--", fg="aquamarine", bg="darkslategray")
label1.pack()

mainWin.configure(background="darkslategray")

mainWin.title('QRcodeGen')

def qcode():
    global e
    string = e.get()
    img = pyqrcode.create(string)
    img.show(img)

e = Entry(mainWin)
e.pack()
e.focus_set()

b = Button(mainWin,text='Generate!',command=qcode, bg="gray")
b.pack(side='top')
mainWin.mainloop()

