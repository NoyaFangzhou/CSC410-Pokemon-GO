#! /usr/bin/python

import cgitb
import cgi
import Cookie
import os
import json # used to send data back in JSON format
import datetime # used to generate the system time

# enable the cgi
cgitb.enable()

login_form = cgi.FieldStorage()

print "Content-type: application/json"

# check the validation of the username and password

# get the stored cookie
stored_cookie_string = os.environ.get('HTTP_COOKIE')

# dictionary to store the response name/value pairs before JSON conversion
# JSON format data that need to send back to client
data = {}

# the client didn't send a cookie
if not stored_cookie_string:
    # print "Hello, You don't have cookie."

    print  # without printing a blank line, the "end of script output before headers" error will occur
    print json.dumps(data)

# else the client DID send a cookie...
else:
    # get the cookie
    cookie = Cookie.SimpleCookie(stored_cookie_string)

    if "user_name" in cookie:
        cookie["user_name"]["expires"] = 'Thu, 01-Jan-1970 00:00:00 GMT'

    if "password" in cookie:
        cookie["password"]["expires"] = 'Thu, 01-Jan-1970 00:00:00 GMT'

    # do some username & password verifications

    print cookie
    print
    print json.dumps(data)



