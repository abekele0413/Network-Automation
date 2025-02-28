
# script.py
import sys
import mysql.connector
import base64
field_name = sys.argv[1]
field_name2 = sys.argv[2]
search_type = sys.argv[3]
DB_Table = sys.argv[4]

try:
	search_box = sys.argv[5]
except:
	search_box=''

#print(DB_Table ,field_name,field_name2)

hashed_password = '<place hashed password here>'
base64_bytes = hashed_password.encode("ascii")
string_bytes = base64.b64decode(base64_bytes)
decoded_password = string_bytes.decode("ascii")
mydb = mysql.connector.connect(host="localhost",user="adrian",password=decoded_password,database='testDB')
mycursor = mydb.cursor()
#describe=mycursor.execute("describe Persons")
#print(describe)
if DB_Table=='Persons':
	if search_box == '':
		mycursor.execute(f"SELECT * FROM {DB_Table}")
		column_names = [description[0] for description in mycursor.description]
	else:
		if search_type =='like':
			mycursor.execute(f"SELECT * FROM {DB_Table} where {field_name} like '%{search_box}%'")
			column_names = [description[0] for description in mycursor.description]
		else:
			mycursor.execute(f"SELECT * FROM {DB_Table} where {field_name} ='{search_box}'")
			column_names = [description[0] for description in mycursor.description]
elif DB_Table=='Persons2':
	if search_box == '':
		mycursor.execute(f"SELECT * FROM {DB_Table}")
		column_names = [description[0] for description in mycursor.description]
	else:
		if search_type =='like':
			mycursor.execute(f"SELECT * FROM {DB_Table} where {field_name2} like '%{search_box}%'")
			column_names = [description[0] for description in mycursor.description]
		else:
			mycursor.execute(f"SELECT * FROM {DB_Table} where {field_name2} ='{search_box}'")
			column_names = [description[0] for description in mycursor.description]

else:
	print('no table found')
myresult = mycursor.fetchall()
if (len(myresult)) ==0:
	print('Nothing Found')
else:
#	print(column_names)
	for x in column_names:
		print(x,' | ')
	print('<br>-------------------------------------------------------------------------------------------------<br>')
	for x in myresult:
		for i in x:
			print(i,',')
		print('<br>')
