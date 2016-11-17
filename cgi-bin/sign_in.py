#!C:\Users\nevgivin\Anaconda2\python.exe

import cgi
import cgitb
import database
import datetime
import hashlib

cgitb.enable()

form = cgi.FieldStorage()


print 'Content-Type: text/html'
print

#USER ID
user_id = form['user_id'].value

#USER PASSPWORD
password = form['password'].value

database.create_table(database.create_user_table)

query = 'select password , salt from user_account where user_ID = \'%s\'' %user_id
result = database.query_table(query)

if result == None:
	info = 'Sorry , we could find your user_ID'
else:
	salt = result[1]
	hasher = hashlib.md5()
	hasher.update(str(password))
	hasher.update(salt)
	encrypted = hasher.hexdigest()
	if encrypted == result[0]:
		info = 'Congratulations, you have logged in'
	else:
		info = 'Wrong password'

	


print '''
<html>
    <head>
        <title>Created Account</title>
    </head>
    <body>
    '''
if info == 'Congratulations, you have logged in':
	print '''
        %s</br>
        You will be redirected to the log_in html </br>
        <meta http-equiv="refresh" content="2;url=../log_in.html">
        '''%info
else:
	print '''
        %s</br>
        Please try again </br>
        <meta http-equiv="refresh" content="2;url=../index.html">
        '''%info
print '''
    </body>
</html>''' 
