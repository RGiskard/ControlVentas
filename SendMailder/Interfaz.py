from tkinter import *
from tkinter import filedialog
import platform
gmailaddress=""
gmailpassword=""
plataform=platform.system()
raiz=Tk()
raiz.title("Mailder")
raiz.resizable(0,0)
raiz.geometry("500x500+300+300")
if plataform=="Windows":
	raiz.iconbitmap("mail.ico")
#miFrame=Frame()
#miFrame.pack()
cuadroCorreo=Entry(raiz,textvariable=gmailaddress)
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
   print(raiz.filename)

botonBuscar=Button(raiz,text="Buscar csv",command = getFile)
botonBuscar.grid(row=2,column=1)
raiz.mainloop()


