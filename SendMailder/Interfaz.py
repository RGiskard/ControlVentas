from tkinter import *
from tkinter import filedialog
import platform

plataform=platform.system()
raiz=Tk()
raiz.title("Mailder")
raiz.resizable(0,0)
raiz.geometry("300x300+300+300")
if plataform=="Windows":
	raiz.iconbitmap("mail.ico")
#miFrame=Frame()
#miFrame.pack()

Keys={}

cuadroCorreo=Entry(raiz)
cuadroCorreo.grid(row=0,column=1,padx=10,pady=10)

correolabel=Label(raiz,text="Correo:  ")
correolabel.grid(row=0,column=0,padx=10,pady=10)

cuadroPasword=Entry(raiz)
cuadroPasword.grid(row=1,column=1,padx=10,pady=10)
cuadroPasword.config(show="*")

passwordlabel=Label(raiz,text="Contraseña:  ")
passwordlabel.grid(row=1,column=0,padx=10,pady=10)

#def codigoBoton():
	#gmailaddress="rcondorib@unsa.edu.pe"

def getFile():
   raiz.filename=filedialog.askopenfilename(initialdir = "/",title = "Seleccione archivos csv",filetypes = (("Archivos csv","*.csv"),("Todos los Archivos","*.*")))
   Keys["gmailaddress"]=cuadroCorreo.get()
   Keys["gmailpassword"]=cuadroPasword.get()
   Keys["ruta"]=raiz.filename


def Execute():   
	print("ruta: "+Keys["ruta"])
	print("gmailaddress: "+Keys["gmailaddress"])
	print("gmailpassword: "+Keys["gmailpassword"])


botonBuscar=Button(raiz,text="Buscar csv",command = getFile)
botonBuscar.grid(row=2,column=1)

botonBuscar=Button(raiz,text="Enviar Correos",command=Execute)
botonBuscar.grid(row=3,column=1)

raiz.mainloop()


