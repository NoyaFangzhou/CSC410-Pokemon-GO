#!C:\Users\nevgivin\Anaconda2\python.exe

import cgi
import cgitb
import userDBManager
import datetime
import hashlib
import json
import Cookie
import os

cgitb.enable()

form = cgi.FieldStorage()

#EMAIL
email_address = form['email'].value

#Team
team = form['team'].value

#USER ID
user_id = form['user_id'].value

#USER NICKNAME
nickname = form['nickname'].value

#USER PASSPWORD
password = form['password'].value

#SALT
salt = str(datetime.datetime.now())



#ENCRYPTED PASSWORD
hasher = hashlib.md5()
hasher.update(str(password))
hasher.update(salt)
encrypted = hasher.hexdigest()

return_data = {}

detect_exist = 'select * from user_account where user_ID = %s'

#database.create_table(database.create_user_table)
exist = userDBManager.query_user(detect_exist, user_id)

if exist != None:
	info = 'Sorry, the user_ID has existed , please try another one'
else:
	sql = 'INSERT INTO user_account (user_ID , password , nickname , salt ,email_address , team) VALUES (%s, %s, %s, %s , %s , %s)'
	insert = userDBManager.create_user(sql,user_id,encrypted,nickname,salt,email_address,team)
	if not insert:
		info = 'An error occur when trying to insert your application to the database'
	else:
		info = 'success'

return_data['result'] = info


# create the cookie
cookie = Cookie.SimpleCookie()
# set the expire date

expires = datetime.datetime.utcnow() + datetime.timedelta(days=5)
cookie['user_name'] = user_id
cookie['password'] = password
cookie['user_name']['expires'] = expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT")
cookie['password']['expires'] = expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT")
return_data['user_name'] = user_id

##http response
print 'Content-Type: application/json'
if cookie and info == 'success':
	print cookie
print
print json.dumps(return_data)
#MiniFieldStorage
