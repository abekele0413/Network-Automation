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



#print(field_name,field_name2,search_type,DB_Table,search_box)

#print(DB_Table ,field_name,field_name2)



#-------------------------------------------------------------------------------------------------------

def dbfunction(hostlocation,username,passwd,dbname,tablename,fieldname):

	

	base64_bytes = passwd.encode("ascii")

	string_bytes = base64.b64decode(base64_bytes)

	decoded_password = string_bytes.decode("ascii")

	mydb = mysql.connector.connect(host=hostlocation,user=username,password=decoded_password,database=dbname)

	mycursor = mydb.cursor()

	if search_box == '':

		mycursor.execute(f"SELECT * FROM {tablename}")

		column_names = [description[0] for description in mycursor.description]

		myresult = mycursor.fetchall()

		if (len(myresult)) ==0:

			print('Nothing Found')

		else:

		#	print(column_names)

			html_output = ""

			for i in column_names:

			    html_output +=  i + ' | '

			

			print(html_output)

			print('-------------------------------------------------------------------------------------------------')

			for x in myresult:

				html_output2 = ''

				for i in x:

					i=str(i)

					html_output2 += i +' , '

				print(html_output2)



	else:



		if search_type =='like':

			mycursor.execute(f"SELECT * FROM {tablename} where {fieldname} like '%{search_box}%'")

			column_names = [description[0] for description in mycursor.description]

			myresult = mycursor.fetchall()

			if (len(myresult)) ==0:

				print('Nothing Found')

			else:

				html_output = ""

				for i in column_names:

					html_output +=  i + ' | '

				

				print(html_output)

				print('-------------------------------------------------------------------------------------------------')

				for x in myresult:

					html_output2 = ''

					for i in x:

						i=str(i)

						html_output2 += i +' , '

					print(html_output2)





		else:



			mycursor.execute(f"SELECT * FROM {tablename} where {fieldname} ='{search_box}'")

			column_names = [description[0] for description in mycursor.description]

			myresult = mycursor.fetchall()

			if (len(myresult)) ==0:

				print('Nothing Found')

			else:

			#	print(column_names)

				html_output = ""

				for i in column_names:

				    html_output +=  i + ' | '

				

				print(html_output)

				print('-------------------------------------------------------------------------------------------------')

				for x in myresult:

					html_output2 = ''

					for i in x:

						i=str(i)

						html_output2 += i +' , '

					print(html_output2)





if DB_Table=='Persons':

	dbfunction('localhost','adrian','password','testDB',DB_Table,field_name)



elif DB_Table=='Persons2':

	dbfunction('localhost','adrian','password','testDB',DB_Table,field_name2)

else:

	print('no table found')

#-------------------------------------------------------------------------------------------------------

