#! /usr/bin/python
import cgi
import cgitb
import Cookie
import os
import json
import hashlib
import friendDBManager
from datetime import datetime

cgitb.enable()
##http response
print "Content-type: application/json"
print


username = None
##retrieve user cookie
stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)
username = cookie['user_name'].value

status = {}
##retrieve post parameter
post_form = cgi.FieldStorage()


user_id = post_form.getvalue('id')
action = post_form.getvalue('follow')


if action == 'false':
	result = friendDBManager.get_team(user_id)

	if result != False:
		status['team'] = result[0]
	else:
		status['team'] = result[0]

	if friendDBManager.if_follow(username ,user_id):
		status['follow'] = 'yes'
	else:
		status['follow'] = 'no'

	print json.dumps(status)
else:
	follow_status = post_form.getvalue('follow_status')

	success_result = None
	if follow_status == 'Follow':
		success_result = 'Unfollow'
	else:
		success_result = 'Follow'

	if follow_status == "Follow":
		result = friendDBManager.add_follow(username , user_id)
	else:
		result = friendDBManager.delete_follow(username , user_id)
	
	if result:
		status['status'] = success_result
	else:
		status['status'] = 'error'
	
	print json.dumps(status)
		

