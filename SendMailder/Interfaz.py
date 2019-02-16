from tkinter import *
from tkinter import filedialog
from gmail import *
import platform
from tkinter import ttk

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
#cuadroPasword.config(show="*")

passwordlabel=Label(raiz,text="Contraseña:  ")
passwordlabel.grid(row=1,column=0,padx=10,pady=10)

#def codigoBoton():
	#gmailaddress="rcondorib@unsa.edu.pe"

def getRuta(path):
	if plataform!="Windows":
		fragments=path.split("/")
		element=fragments[len(fragments)-1]
		return path.replace(element,"")	
	else:
		fragments=path.split("/")#cambiar en caso no funcione \\
		element=fragments[len(fragments)-1]
		return path.replace(element,"")		


def getFile():
   raiz.filename=filedialog.askopenfilename(initialdir = "/",title = "Seleccione archivos csv",filetypes = (("Archivos csv","*.csv"),("Todos los Archivos","*.*")))
   Keys["gmailaddress"]=cuadroCorreo.get()
   Keys["gmailpassword"]=cuadroPasword.get()
   Keys["ruta"]=raiz.filename
   Keys["rutaFiles"]=getRuta(Keys["ruta"])


def Execute(): 
	sentMail(Keys)


botonBuscar=Button(raiz,text="Buscar csv",command = getFile)
botonBuscar.grid(row=2,column=1)

botonBuscar=Button(raiz,text="Enviar Correos",command=Execute)
botonBuscar.grid(row=3,column=1)

raiz.mainloop()


