#! /usr/bin/python
import cgitb
import cgi
import Cookie
import os
import json # used to send data back in JSON format
import verification

cgitb.enable() # enable debugging output in some cases

return_data = {"access" : "permit"}
# get the stored cookie
stored_cookie_string = os.environ.get('HTTP_COOKIE')

if not stored_cookie_string:
	return_data["access"] = "deny"
else:
	cookie = Cookie.SimpleCookie(stored_cookie_string)
	if "user_name" in cookie:
		username = cookie["user_name"].value
	if "password" in cookie:
		password = cookie["password"].value
	
	# do some username & password verifications
	[stat, info] = verification.login_verify(username, password)

	if stat:
		return_data["access"] = "ok"


##http response
print "Content-type: application/json"
print
print json.dumps(return_data)