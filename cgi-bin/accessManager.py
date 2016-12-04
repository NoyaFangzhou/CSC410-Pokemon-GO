#! /usr/bin/python
import cgitb
import cgi
import Cookie
import os
import json # used to send data back in JSON format

cgitb.enable() # enable debugging output in some cases

return_data = {"access" : "permit"}
# get the stored cookie
stored_cookie_string = os.environ.get('HTTP_COOKIE')

if not stored_cookie_string:
	return_data["access"] = "deny"


##http response
print "Content-type: application/json"
print
print json.dumps(return_data)