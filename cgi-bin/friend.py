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

# print json.dumps(post_form.getvalue('show'))
if post_form.getvalue('show') != 'False':
	friends = friendDBManager.query_friend(username)
	if friends == 'Error':
		return_data['result'] = 'failed'

	if friends is not None:
		return_data = json.dumps( [dict(ix) for ix in friends] )

	print json.dumps(return_data)
else:
	if post_form.getvalue('search') != 'False':
		usr_name = post_form.getvalue('name')
		result = friendDBManager.search_user(usr_name)
		
		for ix in result:
			firend_result = friendDBManager.if_follow(username,ix['user_ID'])
			if firend_result:
				ix['follow'] = 'yes'
			else:
				ix['follow'] = 'no'
		print json.dumps( json.dumps(result) )
	else:
		followed_id = post_form.getvalue('follow_id')
		follow_status = post_form.getvalue('follow_status')
		success_result = None
		
		if follow_status == 'Follow':
			success_result = 'Unfollow'
		else:
			success_result = 'Follow'

		if follow_status == "Follow":
			result = friendDBManager.add_follow(username , followed_id)
		else:
			result = friendDBManager.delete_follow(username , followed_id)
		
		if result:
			status['status'] = success_result
		else:
			status['status'] = 'error'
		
		print json.dumps(status)
		