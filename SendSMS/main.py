from connector import *
from sendersms import *
def test():
	C=Connector()
	C.launch()
	S=SenderSMS(C.androidVersion())
	total=5;
	numbers=[]
	for i in range(total):
		numbers.append("123456789")
	#sms=prepareSMS(body)
	id=1
	for number in numbers:
		body="Es tes un mensaje "+str(id)+" de "+str(total)
		id=id+1
		sms=prepareSMS(body)
		S.sendSMS(number,sms)
		time.sleep(2)
	print("Envios terminados")
	
