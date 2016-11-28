#! /usr/bin/python
import cgi
import cgitb
import Cookie
import os
import json
import postDBManager
from datetime import datetime

cgitb.enable()

##global variables
username = None
return_data = {}

##retrieve user cookie
stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)
username = cookie['user_name'].value

##retrieve post parameter
post_form = cgi.FieldStorage()

##create new post send by user
if post_form.getvalue('new'):
	##the json data contains post info, will be return to user
	post_data = {}

	post_data['author'] = username
	
	if post_form.getvalue('post-content') == None:
		post_data['content'] = ''
	else:
		post_data['content'] = post_form.getvalue('post-content')
	
	post_data['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	post_data['likes'] = 0

	if not postDBManager.insert_post(post_data):
		#if db insertion failed, return inform user with another json 
		post_data = {'result' : 'false'}
	else:
		post_data['result'] = 'true'
	
	return_data = post_data

##retrieve old posts
else:

	old_posts = postDBManager.query_post(username)
	
	if old_posts != None:
		for post in old_posts:
			post['date'] = str(post['date'])
	
	return_data = json.dumps( [dict(ix) for ix in old_posts] )

##http response
print "Content-type: application/json"
print
print json.dumps(return_data)