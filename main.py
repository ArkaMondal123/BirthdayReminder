#importing requests
import requests

#importing os
import os

#checking internet status

def internetCheck():
	try:
		requests.get(url = "https://arkamondal123.github.io")
		return False
	except:
		return True

if internetCheck():
	troubleshoot = os.system("msdt.exe /id NetworkDiagnosticsWeb")
	print("awaiting internet connection...")


while internetCheck():
	pass

print("Connection Established!")




#external modules
try:
	import pywhatkit
except:
	print("error with pywhatkit")
	while 1>0:
		pass



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
				'4/15' : '+919538848338'
				}

try:
	#Retrieving today's date
	today = date.today()
	check_str = f"{today.month}/{today.day}"


	for i in birthdays.keys():
		if list(map(int, i.split("/"))) == list(map(int, check_str.split('/'))):
			datetime_india = datetime.now(pytz.timezone('Asia/Kolkata'))
			t = list(map(int, datetime_india.strftime('%H:%M').split(":")))
			if check_str == "4/15":
				pywhatkit.sendwhatmsg(birthdays[check_str], "its brocode's birthday", t[0], t[1]+2)
			else:
				pywhatkit.sendwhatmsg(birthdays[check_str], "Happy birthday bro", t[0], t[1]+2)


except:
	print("error with code")
	while 1>0:
		pass


	
