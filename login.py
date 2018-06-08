#!/usr/bin/python3
import cgi
import cgitb
import time
import mysql.connector as mysql
print("Content-type:text/html")
print("")
cgitb.enable()
web_data=cgi.FieldStorage()
login_email=web_data.getvalue('login_email')
login_password=web_data.getvalue('login_password')
# print(login_email)
# print(login_password)
try:
    conn=mysql.connect(user='root',password='password',database='cgi',host='localhost')
    if conn.is_connected():
        print("Connected")
        curs=conn.cursor()
        curs.execute("SELECT * FROM cgi_info WHERE email = %s AND password = %s", [login_email, login_password])
        if login_email==None | login_password==None:
            print("Please enter valid credentials..")
        else:
            if curs.fetchone() is not None:
                print("Logging you in..")
                time.sleep(2)
                redirectURL = "http://127.0.0.1/dashboard.html"
                print('<html>')
                print('  <head>')
                print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')
                print('  </head>')
                print('</html>')
            else:
                print("Invalid details...")
                time.sleep(2)
                redirectURL = "http://127.0.0.1/login.html"
                print('<html>')
                print('  <head>')
                print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')
                print('  </head>')
                print('</html>')
except:
    print("unable to fetch data")
