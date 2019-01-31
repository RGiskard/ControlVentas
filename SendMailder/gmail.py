##Dependecias

import smtplib 
import pandas as pd
from values import *
from email.mime.multipart import MIMEMultipart
#from email.MIMEText import MIMEText
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Etablece importacion tkinker windows linux
import platform
plataform=platform.system()



def sentMail(gmailaddress,gmailpassword):
	cereal_df = pd.read_csv("mails.csv")
	cabecera=["DNI","Nombre","Correo","Asunto","msg","Archivo"]
	for index, row in cereal_df.iterrows():
		####Construccipon del enviador con subject
		msg = MIMEMultipart()
		msg['From'] = gmailaddress
		msg['To'] = row['Correo'] 
		msg['Subject'] ="Boleta "+row['Asunto']
		body = "Estimado: "+row['Nombre']+"\nAdjunto en el presente mensaje encontrará su boleta del mes de: "+row['Asunto']+"\nMuchas Gracias por su Preferencia\n No es necesario responder a este mensaje"
		msg.attach(MIMEText(body, 'plain'))
		filename = row['Archivo']+".pdf"#archivo a enviar
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
		mailServer.sendmail(gmailaddress, row['Correo'] , text)
		print(" \n Sent!")
		mailServer.quit()



