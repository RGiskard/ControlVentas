##Dependecias

import smtplib 
import pandas as pd
from values import *
from email.mime.multipart import MIMEMultipart
#from email.MIMEText import MIMEText
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

cereal_df = pd.read_csv("mails.csv")
cabecera=["correo","Asunto","msg"]
#mailto = input("what email address do you want to send your message to? \n ")
#msg = input("What is your message? \n ")

#mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
#mailServer.starttls()
#mailServer.login(gmailaddress , gmailpassword)
#mailServer.sendmail(gmailaddress, mailto , msg)
#print(" \n Sent!")
#mailServer.quit()



def sentMail():
	for index, row in cereal_df.iterrows():
		####Construccipon del enviador con subject
		msg = MIMEMultipart()
		msg['From'] = gmailaddress
		msg['To'] = row['correo'] 
		msg['Subject'] = row['Asunto']
		body = row['msg']+row['correo']
		msg.attach(MIMEText(body, 'plain'))
		filename = "ravelbolero.pdf"#archivo a enviar
		#attachment = open("/home/moebius/Documentos/ControlVentas/SendMailder", "rb")#directorio
		attachment = open(filename, "rb")
		#codificacion
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		msg.attach(part)
		###Fin construcción
		###Construcción de bloque para enviar archivo adjunto
		##Fin archivo adjunto
		text = msg.as_string()
		mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
		mailServer.starttls()
		mailServer.login(gmailaddress , gmailpassword)
		mailServer.sendmail(gmailaddress, row['correo'] , text)
		print(" \n Sent!")
		mailServer.quit()

import platform
plataform=platform.system()

if plataform=="Windows":
	from tkinter import *

else:
	from Tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.hi_there = Button(frame, text="Hello World", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
    def say_hi(self):
        print ("hola todo el mundo!")

root = Tk()
app = App(root)
root.mainloop()

