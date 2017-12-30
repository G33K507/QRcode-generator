from Tkinter import *
import pyqrcode
import png
#----The Window----#
mainWin = Tk()
mainWin.title('QRcodeGen')
mainWin.minsize(300,100)
mainWin.configure(background="darkslategray")
#----Custom Function For Generating The QRcode----#
def qcode():
    global e
    string = e.get()
    img = pyqrcode.create(string)
    img.show(img)
#----The Label----#
label1 = Label(mainWin, text="--Input--", fg="aquamarine", bg="darkslategray")
label1.pack()
#----The Entry Field---#
e = Entry(mainWin)
e.pack()
e.focus_set()
#----The Button----#
b = Button(mainWin,text='Generate!',command=qcode, bg="gray")
b.pack(side='top')

mainWin.mainloop()
