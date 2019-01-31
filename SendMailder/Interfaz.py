from tkinter import *
import platform
plataform=platform.system()
raiz=Tk()
raiz.title("Mailder")
raiz.resizable(0,0)
raiz.geometry("500x500+300+300")
if plataform=="Windows":
	raiz.iconbitmap("mail.ico")
miFrame=Frame()
miFrame.pack()

raiz.mainloop()




