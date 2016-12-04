#! /usr/bin/python
import cgi
import cgitb
import Cookie
import os
import json
import hashlib
import profileDBManager
from datetime import datetime

cgitb.enable()
##http response
print "Content-type: application/json"
print
##global variables
username = None
return_data = {}
update = {}
status = {}
##retrieve user cookie
stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)
username = cookie['user_name'].value





##retrieve post parameter
post_form = cgi.FieldStorage()

if post_form.getvalue('modify') != 'False':
	if post_form.getvalue('change_password'):	
		
		password = post_form.getvalue('change_password')

		#SALT
		salt = str(datetime.now())

		#ENCRYPTED PASSWORD
		hasher = hashlib.md5()
		
		hasher.update(str(password))
		hasher.update(salt)
		
		encrypted = hasher.hexdigest()
		if profileDBManager.change_password(username , encrypted , salt):
			status['status'] = 'true'
		else:
			status['status'] = 'false'
		print json.dumps(status)
	else:
		update['nickname'] = post_form.getvalue('nickname')
		update['email_address'] = post_form.getvalue('email_address')
		# update['team'] = post_form['team'].value

		if profileDBManager.update(username , update):
			status['status'] = 'true'
		else:
			status['status'] = 'false'

		status = json.dumps(status)
		print status
else:
	profile = profileDBManager.query_profile(username)
	return_data = json.dumps( profile )
# print return_data
	print json.dumps(return_data)
