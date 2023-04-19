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
birthdays = {'10/3' : '+917975511796', 
				'8/08' : '+919632857569',
				'8/20' : '+918073201289',
				'1/23' : '+918618450647',
				'3/14' : '+918867829602',
				'3/23' : '+918904011620',
				'2/09' : '+918001700808',
				'9/09' : '+919986601859',
				'4/15' : '+919538848338',
				'4/16' : '+919538848338'}


#Retrieving today's date
today = date.today()
check_str = f"{today.month}/{today.day}"


for i in birthdays.keys():
	if list(map(int, i.split("/"))) == list(map(int, check_str.split('/'))):
		datetime_india = datetime.now(pytz.timezone('Asia/Kolkata'))
		t = list(map(int, datetime_india.strftime('%H:%M').split(":")))
		if check_str == "4/15" or check_str == "5/15":
			pywhatkit.sendwhatmsg(birthdays[check_str], "its brocode's birthday", t[0], t[1]+2)
		else:
			pywhatkit.sendwhatmsg(birthdays[check_str], "Happy birthday bro", t[0], t[1]+2)




