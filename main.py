#internet check module
import socket

#checking internet status
offline = False

IPaddress=socket.gethostbyname(socket.gethostname())
if IPaddress=="127.0.0.1":
    offline = True
else:
    offline = False

run = 0
while offline:
	IPaddress=socket.gethostbyname(socket.gethostname())
	if IPaddress=='127.0.0.1':
		if run==0:
			print("awaiting internet connection...")
		run+=1

	else:
		print("Connection Established!")
		offline = False





#external modules (excluding socket)
import pywhatkit


#internal modules
import pytz
from datetime import date, datetime



#Birthday List
birthdays = {'mm/dd' : '+91xxxxxxxxxx'}


#Retrieving today's date
today = date.today()
check_str = f"{today.month}/{today.day}"


for i in birthdays.keys():
	if list(map(int, i.split("/"))) == list(map(int, check_str.split('/'))):
		datetime_india = datetime.now(pytz.timezone('Asia/Kolkata'))
		t = list(map(int, datetime_india.strftime('%H:%M').split(":")))
		pywhatkit.sendwhatmsg(birthdays[check_str], "Happy birthday", t[0], t[1]+2)




