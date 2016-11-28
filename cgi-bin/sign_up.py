#! /usr/bin/python

import cgi
import cgitb
import userDBManager
import datetime
import hashlib


cgitb.enable()

form = cgi.FieldStorage()


print 'Content-Type: text/html'
print

#USER ID
user_id = form['user_id'].value

#USER NICKNAME
nickname = form['nickname'].value

#USER PASSPWORD
password = form['password'].value

#PASSWORD1
re_password = form['re_password'].value


#SALT
salt = str(datetime.datetime.now())

#ENCRYPTED PASSWORD
hasher = hashlib.md5()
hasher.update(str(password))
hasher.update(salt)
encrypted = hasher.hexdigest()


flag = 0

detect_exist = 'select * from user_account where user_ID = %s'

#database.create_table(database.create_user_table)
exist = userDBManager.query_user(detect_exist, user_id)

if exist != None:
	info = 'Sorry, the user_ID has existed , please try another one</br>'
else:
	if re_password != password:
		info = 'Two passwords are not same'
	else:
		sql = 'INSERT INTO user_account (user_ID , password , nickname , salt) VALUES (%s, %s, %s, %s)'
		insert = userDBManager.create_user(sql,user_id,encrypted,nickname,salt)
		if not insert:
			info = 'An error occur when trying to insert your application to the database'
		else:
			info = 'Congratulations , your account has been created</br>'
			flag = 1

print '''
<html>
    <head>
        <title>Created Account</title>
    </head>
    <body>
        %s</br>
     '''%info
        
if flag == 1:
	print 'You will be redirected to the log_in html'
	print '<meta http-equiv="refresh" content="5;url=../index.html">'

print ''' 
    </body>
</html>''' 












#MiniFieldStorage
