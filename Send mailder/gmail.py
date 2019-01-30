##Dependecias

import smtplib 
import pandas as pd
from values import *
from email.mime.multipart import MIMEMultipart
#from email.MIMEText import MIMEText
from email.mime.text import MIMEText

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




for index, row in cereal_df.iterrows():
	####Construccipon del enviador con subject
	msg = MIMEMultipart()
	msg['From'] = gmailaddress
	msg['To'] = row['correo'] 
	msg['Subject'] = row['Asunto']
	body = row['msg']+row['correo']
	msg.attach(MIMEText(body, 'plain'))
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
