#!C:\Users\nevgivin\Anaconda2\python.exe
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

##retrieve post parameter
post_form = cgi.FieldStorage()

##create new post send by user
if post_form.getvalue('new'):
	##retrieve user cookie
	stored_cookie_string = os.environ.get('HTTP_COOKIE')
	cookie = Cookie.SimpleCookie(stored_cookie_string)
	username = cookie['user_name'].value
	##the json data contains post info, will be return to user
	post_data = {}

	post_data['author'] = username
	
	if post_form.getvalue('post-content') == None:
		post_data['content'] = ''
	else:
		post_data['content'] = post_form.getvalue('post-content')
	
	post_data['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	post_data['likes'] = 0

	result, post_id = postDBManager.insert_post(post_data)

	if not result:
		#if db insertion failed, return inform user with another json 
		post_data['result'] = 'failed'
	else:
		post_data['result'] = 'succeed'
		post_data['id'] = post_id
	
	return_data = post_data

##retrieve old posts
elif post_form.getvalue('retrieve'):
	##retrieve user cookie
	stored_cookie_string = os.environ.get('HTTP_COOKIE')
	cookie = Cookie.SimpleCookie(stored_cookie_string)
	username = cookie['user_name'].value

	old_posts = postDBManager.query_post(username)
	if old_posts == 'Error':
		return_data['result'] = 'failed'

	if old_posts is not None:
		for post in old_posts:
			post['date'] = str(post['date'])
		return_data = json.dumps( [dict(ix) for ix in old_posts] )

#delete one post
elif post_form.getvalue('delete'):
	post_id = post_form.getvalue('id');
	result = postDBManager.delete_post(post_id);
	if result == True:
		return_data = {"result" : "succeed"}
	else:
		return_data = {"result" : "failed"}

elif post_form.getvalue('like'):
	post_id = post_form.getvalue('id');
	result = postDBManager.do_like(post_id);
	if not result:
		return_data['result'] = 'failed'
	else:
		return_data['result'] = 'succeed'

##http response
print "Content-type: application/json"
print
print json.dumps(return_data)