#python /mnt/c/Users/adri9996/Documents/test5.py
devicenum = raw_input('enter device number:')
print 'running script....' 
from pykeepass import PyKeePass
import os
pw = raw_input('enter keepass password:')
kp = PyKeePass('/mnt/c/Users/adri9996/downloads/Database.kdbx', password=pw)
device = kp.find_entries(string={'device number': devicenum}, first=True)
deviceuser = device.username
devicepw = device.password
deviceip = device.url
devicetitle = device.title
customer = device.group
customer = str(customer)[7:]
print '\n',40 * '-','\ncustomer: '+customer,'\ndevice ip: '+deviceip, '\nusername: '+deviceuser, '\npassword: '+'*******', '\n',40 * '-','\n'
os.system('sshpass -p '+devicepw +' ssh '+deviceuser+'@'+deviceip)

