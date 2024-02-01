#python3 /mnt/c/Users/abekele/'OneDrive - VMware, Inc'/Documents/ssh.py

import netmiko
import time
from getpass import getpass
import os
import threading
import base64

passwdgetpass = getpass()
password = passwdgetpass
username = "admin"





#devices_list = {"ise03":"<ip address>"}
#devices_list = {"ise04":"<ip address>","ise03":"<ip address>"}
devices_list = {"ise-sc2-pan-1":"<ip address>", "ise-wdc-pan-1":"<ip address>", "ise-sc2-mnt-1":"<ip address>", "ise-wdc-mnt-1":"<ip address>", "ise-sc2-psn-1":"<ip address>", "ise-wdc-psn-1":"<ip address>", "ise-ams2-psn-1":"<ip address>", "ise-blr3-psn-1":"<ip address>", "ise-sof2-psn-1":"<ip address>"} 
#devices_list = {"ise-ams2-psn-1":"<ip address>"} 
counter=1
command = "show application status ise | i Application"
#command = """show memory | i "free memory:""""
#command = "show version | i Version"


# Define a function for the thread
def sshing( delay, devicename):
	time.sleep(delay)
	net_connect = netmiko.ConnectHandler(device_type="cisco_ios", host=devices_list[devicename], username=username, password=password)
	prompt= net_connect.find_prompt()
	prompt=str(prompt)
	output = net_connect.send_command(command,read_timeout=20)
	print(60*'=','\n',devicename,devices_list[devicename],prompt,'\n',40*'-','\n',output)
	net_connect.disconnect()
	

while(True):
	print(time.ctime())
	print("Ran %s times" %(counter))
	print("don't kill script\nrunning commands......")
#	lab1 = threading.Thread(target=sshing, args=(1, "ise04"))
#	lab2 = threading.Thread(target=sshing, args=(1, "ise03"))
#	lab1.start()
#	lab2.start()
#	lab1.join()
#	lab2.join()
	prod1 = threading.Thread(target=sshing, args=(1, "ise-sc2-pan-1"))
	prod2 = threading.Thread(target=sshing, args=(1, "ise-wdc-pan-1"))
	prod3 = threading.Thread(target=sshing, args=(1, "ise-sc2-mnt-1"))
	prod4 = threading.Thread(target=sshing, args=(1, "ise-wdc-mnt-1"))
	prod5 = threading.Thread(target=sshing, args=(1, "ise-sc2-psn-1"))
	prod6 = threading.Thread(target=sshing, args=(1, "ise-wdc-psn-1"))
	prod7 = threading.Thread(target=sshing, args=(1, "ise-ams2-psn-1"))
	prod8 = threading.Thread(target=sshing, args=(1, "ise-blr3-psn-1"))
	prod9 = threading.Thread(target=sshing, args=(1, "ise-sof2-psn-1"))
	prod1.start()
	prod2.start()
	prod3.start()
	prod4.start()
	prod5.start()
	prod6.start()
	prod7.start()
	prod8.start()
	prod9.start()
	prod1.join()
	prod2.join()
	prod3.join()
	prod4.join()
	prod5.join()
	prod6.join()
	prod7.join()
	prod8.join()
	prod9.join()
	counter+=1
	print('\n',60*'=','\n',60*'=','\n',60*'=','\n','Done! Waiting 15 seconds, you can kill script')
	time.sleep(15)
	os.system("clear")







