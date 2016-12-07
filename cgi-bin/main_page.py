#! /usr/bin/python

# use cookie for persistant data storage
# if no cookie, return the login page
# if has cookie, return the main page and change the name_logo field with user_name

import cgitb
import cgi
import Cookie
import os
import json # used to send data back in JSON format
import datetime # used to generate the system time
import verification

cgitb.enable() # enable debugging output in some cases

login_form = cgi.FieldStorage()

print "Content-type: application/json"
print # without printing a blank line, the "end of script output before headers" error will occur

# get the stored cookie
stored_cookie_string = os.environ.get('HTTP_COOKIE')

# dictionary to store the response name/value pairs before JSON conversion
# JSON format data that need to send back to client
data = {}

# the client didn't send a cookie
if not stored_cookie_string:
  data = {}

  # print "Hello, You don't have cookie."

  data['user_name'] = "nil"

  print json.dumps(data)

# else the client DID send a cookie...
else:
  # get the cookie
  cookie = Cookie.SimpleCookie(stored_cookie_string)

  data = {}

  if "user_name" in cookie:
    username = cookie["user_name"].value

  if "password" in cookie:
    password = cookie["password"].value

  # do some username & password verifications
  [stat, info] = verification.login_verify(username, password)

  if stat:
    data['user_name'] = username
  
  data['result'] = info

  print json.dumps(data)

    

