#! /usr/bin/python

import cgi
import cgitb
import userDBManager
import datetime
import hashlib
import json
import Cookie
import os

cgitb.enable()

##http response
print 'Content-Type: application/json'

form = cgi.FieldStorage()


#USER ID
user_id = form['user_id'].value

#USER NICKNAME
nickname = form['nickname'].value

#USER PASSPWORD
password = form['password'].value

#email
email = form['email'].value

#team
team = form['team'].value

#SALT
salt = str(datetime.datetime.now())



#ENCRYPTED PASSWORD
hasher = hashlib.md5()
hasher.update(str(password))
hasher.update(salt)
encrypted = hasher.hexdigest()

return_data = {}
info = '';

detect_exist = 'select * from user_account where user_ID = %s'

#database.create_table(database.create_user_table)
exist = userDBManager.query_user(detect_exist, user_id)

if exist != None:
	info = 'Sorry, the user_ID has existed , please try another one'
else:
	sql = 'INSERT INTO user_account (user_ID , password , nickname , salt, email_address, team) VALUES (%s, %s, %s, %s, %s, %s)'
	insert = userDBManager.create_user(sql,user_id,encrypted,nickname,salt,email,team)
	if not insert:
		info = 'An error occur when trying to insert your application to the database'
	else:
		cookie = Cookie.SimpleCookie()
		cookie['user_name'] = user_id
		cookie['password'] = password
		info = 'success'
		print cookie
		return_data['user_name'] = user_id

return_data['result'] = info

print
print json.dumps(return_data)
#MiniFieldStorage
