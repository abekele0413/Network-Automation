import json

import sys

import mysql.connector

import base64



DB_Table = sys.argv[1]





def dbfunction(hostlocation,username,passwd,dbname,tablename):

	base64_bytes = passwd.encode("ascii")

	string_bytes = base64.b64decode(base64_bytes)

	decoded_password = string_bytes.decode("ascii")

	mydb = mysql.connector.connect(host=hostlocation,user=username,password=decoded_password,database=dbname)

	mycursor = mydb.cursor()

	

	mycursor.execute(f"SELECT * FROM {tablename}")

	column_names = [description[0] for description in mycursor.description]

	print(json.dumps(column_names))

		

if DB_Table=='Persons':

	dbfunction('localhost','adrian','password','testDB',DB_Table)

elif DB_Table=='Persons2':

	dbfunction('localhost','adrian','password','testDB',DB_Table)

