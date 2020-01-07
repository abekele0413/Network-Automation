#python /mnt/c/Users/adri9996/Documents/test5.py
import getpass
hashpassword = getpass.getpass(b'keepass password:')
#hashpassword = b'0'
devicenum = raw_input('enter device number:')
print 'running script....' 
from cryptography.fernet import Fernet
from pykeepass import PyKeePass
import pyperclip
import re
import os
key = b'IpDlPNMtfsR2Uu6esQtx70o4mb6EDU2KWk8Su2tT7XY='
cipher_suite = Fernet(key)
ciphered_text1 = b'gAAAAABeC2GFDDsiJ55to82BZwWVNhgySRW76'
ciphered_text2 = b'F7jM5aI9FKWAZ3R9I7TQrrN7S04V0BNZzjjYldWi2VpvK-lYgxbEEYkmGGyQ=='
hashpassword = ciphered_text1+hashpassword+ciphered_text2
#=========function2======================================================	
def function2():
	deviceuser = device.username
	devicepw = device.password
	deviceip = device.url
	JH = 'None'
	JH = device.get_custom_property('JH')
	JH = str(JH)
	JH = JH.lower()
	devicetitle = device.title
	enablepw = 'None'
	enablepw = device.get_custom_property('enable password')
	enablepw = str(enablepw)
	devicenumber = device.get_custom_property('device number')
	customer = device.group
	customer = str(customer)[7:]
	try:
		device.notes
	except:
		devicenotes = 'None'
	else:
		devicenotes = str(device.notes)
	print '\n',40 * '-','\nDevice Number: '+devicenumber,'\nCustomer: '+customer,'\nDevice Name: '+devicetitle, '\nDevice ip: '+deviceip
	
	if deviceuser.lower() == 'tacacs':
		print 'Username: Tacacs'
		print 'Password: Tacacs'
		print 'Notes: \n'+devicenotes,'\n',40 * '-'
		if JH == 'none':
			deviceuser = raw_input('Enter Tacacs username:')
			devicepw = getpass.getpass('Enter Tacacs password:')
			
			os.system('sshpass -p '+devicepw +' ssh '+deviceuser+'@'+deviceip)

		else:
			JumpH = kp.find_entries(title='jumphost', first=True)
			JumpHip = str(JumpH.url)
			JumpHusername = str(JumpH.username)
			JumpHdomain = str(JumpH.get_custom_property('domain'))
			JumpHnotes = str(JumpH.notes)
			print '!'*40,'\nMust connect to Jumphost '+JumpHip + '\n','!'*40,'\n',40 * '-'+'\nJH Username: '+JumpHusername+'\nJH Domain: '+JumpHdomain +'\nJH Notes: '+JumpHnotes +  '\n',40 * '-'

	elif enablepw == 'None':
		print 'Username: '+deviceuser
		if JH == 'none':
			print 'Password: ******* (In your clipboard)'
			print 'Notes: \n'+devicenotes,'\n',40 * '-'
			pyperclip.copy(devicepw)
			
			os.system('sshpass -p '+devicepw +' ssh '+deviceuser+'@'+deviceip)

		else:
			JumpH = kp.find_entries(title='jumphost', first=True)
			JumpHip = str(JumpH.url)
			JumpHusername = str(JumpH.username)
			JumpHdomain = str(JumpH.get_custom_property('domain'))
			JumpHnotes = str(JumpH.notes)
			print 'Password: ******* '
			print 'Notes: \n'+devicenotes,'\n',40 * '-'
			print '!'*40,'\nMust connect to Jumphost '+JumpHip + '\n','!'*40,'\n',40 * '-'+'\nJH Username: '+JumpHusername+'\nJH Domain: '+JumpHdomain +'\nJH Notes: '+JumpHnotes +  '\n',40 * '-'
	else:
		print 'Username: '+deviceuser
		if JH == 'none':
			pyperclip.copy(enablepw)
			print 'Password: ******* \nEnable: ******* (In your clipboard)'
			print 'Notes: \n'+devicenotes,'\n',40 * '-'
			
			os.system('sshpass -p '+devicepw +' ssh '+deviceuser+'@'+deviceip)

		else:
			JumpH = kp.find_entries(title='jumphost', first=True)
			JumpHip = str(JumpH.url)
			JumpHusername = str(JumpH.username)
			JumpHdomain = str(JumpH.get_custom_property('domain'))
			JumpHnotes = str(JumpH.notes)
			print 'Password: ******* \nEnable: ******* '
			print 'Notes: \n'+devicenotes,'\n',40 * '-'	
			print '!'*40,'\nMust connect to Jumphost '+JumpHip + '\n','!'*40,'\n',40 * '-'+'\nJH Username: '+JumpHusername+'\nJH Domain: '+JumpHdomain +'\nJH Notes: '+JumpHnotes +  '\n',40 * '-'
#=========function2======================================================


#-------------------------checks password------------------------------------
try:
	(cipher_suite.decrypt(hashpassword))
except:
	print '\n'+'#'*35+'\n####  Incorrect Password Kosta ####'+'\n'+'#'*35+'\nTry again'
	hashpassword = getpass.getpass(b'keepass password:')
	hashpassword = ciphered_text1+hashpassword+ciphered_text2
	#-------------------------checks password------------------------------------	
	try:
		(cipher_suite.decrypt(hashpassword))
	except:
		print '\n'+'#'*35+'\n####  Incorrect Password Kosta ####'+'\n'+'#'*35
	else:
		pw = (cipher_suite.decrypt(hashpassword))
		kp = PyKeePass('/mnt/c/Users/adri9996/downloads/Database.kdbx', password=pw)
		device = kp.find_entries(string={'device number': devicenum}, first=True)
	#-------------------------checks device------------------------------------
		try:
			device.username
		except:
			print '\n'+'#'*40+'\n####  Incorrect device number Kosta ####'+'\n'+'#'*40+'\nTry again'
			devicenum2 = raw_input('enter device number:')
			device = kp.find_entries(string={'device number': devicenum2}, first=True)
	#-------------------------checks device------------------------------------
			try:
				device.username
			except:
				print '\n'+'#'*40+'\n####  Incorrect device number Kosta ####'+'\n'+'#'*40
			else:
				function2()
		else:
			function2()	
else:
	pw = (cipher_suite.decrypt(hashpassword))
	kp = PyKeePass('/mnt/c/Users/adri9996/downloads/Database.kdbx', password=pw)
	device = kp.find_entries(string={'device number': devicenum}, first=True)
	#-------------------------checks device------------------------------------
	try:
		device.username
	except:
		print '\n'+'#'*40+'\n####  Incorrect device number Kosta ####'+'\n'+'#'*40+'\nTry again'
		devicenum2 = raw_input('enter device number:')
		device = kp.find_entries(string={'device number': devicenum2}, first=True)
	#-------------------------checks device------------------------------------
		try:
			device.username
		except:
			print '\n'+'#'*40+'\n####  Incorrect device number Kosta ####'+'\n'+'#'*40
		else:
			function2()
	else:
		function2()

	
	
	


#----------------------------------------------------------------------------------------
#!!!!!!!!!!!!!for encrypting the password 
#!!!!!!!!!!!!!generate key
#from cryptography.fernet import Fernet
#key = Fernet.generate_key()
#print(key)

#!!!!!!!!!!!!!encrypt

#from cryptography.fernet import Fernet
#key = b'pRmgMa8T0INjEAfksaq2aafoOHHoiq320r9f9fhQDIONc1F8AY='
#cipher_suite = Fernet(key)
#ciphered_text = cipher_suite.encrypt(b"EnterPasswordHere")   #required to be bytes
#print(ciphered_text) 

#!!!!!!!!!!!!!decrypt

#from cryptography.fernet import Fernet
#key = b'IpDlPNMtfsR2Uu6esQtx70o4mb6EDU2KWk8Su2tT7XY='
#cipher_suite = Fernet(key)
#ciphered_text = b'gAAAAABeC2GFDDsiJ55to82BZwWVNhgySRW760F7jM5aI9FKWAZ3R9I7TQrrN7S04V0BNZzjjYldWi2VpvK-lYgxbEEYkmGGyQ=='
#pw = (cipher_suite.decrypt(ciphered_text))


#connection = netmiko.ConnectHandler(ip='10.127.2.12', device_type='cisco_asa',username = 'rack' ,password = 'rack9155', secret = 'rack9155')
#shell = spur.SshShell(hostname="10.127.2.12", username="rack", password="rack9155").run
#result = shell.run(["ascp.exe", directory, "Ausername@10.0.0.1:/"], stdout=sys.stdout, update_env=environment)
#result = shell.run(["echo", "-n", "hello"])
#print result.output # prints hello
#subprocess.run(["ssh", "rack@10.127.2.12", "rack9155"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
#
#connect(self, hostname, port=22, username=None, password=None,
#        pkey=None, key_filename=None, timeout=None, allow_agent=True,
#        look_for_keys=True, compress=False)
#
#client = SSHClient()
#client.load_system_host_keys()
#client.connect('ssh.example.com')
#stdin, stdout, stderr = client.exec_command('ls -l')
#
#environment = {}
#environment["ASPERA_SCP_PASS"] = "password"
#shell = spur.SshShell(hostname="10.127.2.12", username="rack", password="rack9155", stdout=sys.stdout)
#
#sshpass -p 'rack9155' ssh rack@10.127.2.11
