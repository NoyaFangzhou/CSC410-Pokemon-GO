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

##retrieve post parameter
post_form = cgi.FieldStorage()

##http response
print "Content-type: application/json"
print

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
	
	if "pic" in post_form:
		post_data['pic'] = "true"

	result, post_id = postDBManager.insert_post(post_data)

	if not result:
		#if db insertion failed, return inform user with another json 
		post_data['result'] = 'failed'
	else:
		if post_form.getvalue('pic'):
			target = open("../pictures/" + str(post_id),"wb")
			target.write(post_form['pic'].value)
			post_data['img'] = 'pictures/' + str(post_id)
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
			if post['img'] == 1:
				post['img'] = 'pictures/' + str(post['id'])
		return_data = json.dumps( [dict(ix) for ix in old_posts] )

#delete one post
elif post_form.getvalue('delete'):
	post_id = post_form.getvalue('id')
	result = postDBManager.delete_post(post_id)
	if result == True:
		files = os.listdir("../pictures")
		for file in files:
			if file == post_id:
				os.remove("../pictures/" + file)
		return_data = {"result" : "succeed"}
	else:
		return_data = {"result" : "failed"}

#like a post
elif post_form.getvalue('like'):
	##retrieve user cookie
	stored_cookie_string = os.environ.get('HTTP_COOKIE')
	cookie = Cookie.SimpleCookie(stored_cookie_string)
	post_id = post_form.getvalue('id')
	liker_id = cookie['user_name'].value
	result = postDBManager.do_like(post_id, liker_id)
	if not result:
		return_data['result'] = 'failed'
	elif result == "No change":
		return_data['result'] = 'no change'
	else:
		return_data['result'] = 'succeed'

#show posts of friend
elif post_form.getvalue('friend-post'):
	friend_id = post_form.getvalue('id')
	##retrieve friend post from DB
	friend_posts = postDBManager.query_post(friend_id)
	if friend_posts == 'Error':
		return_data['result'] = 'failed'
	
	if friend_posts is not None:
		for post in friend_posts:
			post['date'] = str(post['date'])
			if post['img'] == 1:
				post['img'] = 'pictures/' + str(post['id'])
		return_data = json.dumps( [dict(ix) for ix in friend_posts] )


print json.dumps(return_data)
