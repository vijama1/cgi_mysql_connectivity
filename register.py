#!/usr/bin/python3
import cgi
import cgitb
import mysql.connector as mysql
print("Content-type:text/html")
print("")
cgitb.enable()
web_data=cgi.FieldStorage()
name=web_data.getvalue('name')
number=int(web_data.getvalue('number'))
email=web_data.getvalue('email')
password=web_data.getvalue('password')

conn=mysql.connect(user='root',password='password',database='cgi',host='localhost')
if conn.is_connected():
    print("Connected")
    curs=conn.cursor()
    #query='INSERT INTO cgi_info VALUES("%s","%d","%s","%s")'%(name,number,email,password))
    out = curs.execute('insert into cgi_info values("%s","%d","%s","%s")'%(name,number,email,password))
    conn.commit()
else:
    print("Not Connected")
