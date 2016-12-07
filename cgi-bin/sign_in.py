#! /usr/bin/python

import cgitb
import cgi
import Cookie
import os
import json # used to send data back in JSON format
import datetime # used to generate the system time
# import database # used to interact with database
import hashlib # used to cypt the password
import verification

# enable the cgi
cgitb.enable()

login_form = cgi.FieldStorage()

# check the validation of the username and password
data = {}
usrname = login_form["user_id"].value # get the username from the table
pwd = login_form["password"].value # get the password from the table
remember = login_form["remember_me"].value # get whether use status saving
#
print "Content-type: application/json"

# print  # without printing a blank line, the "end of script output before headers" error will occur
# if the remember me checkbox was clicled, set the cookie

# do some username & password verifications
[stat, info] = verification.login_verify(usrname, pwd)

if remember == "true":
    # print "Hello, I send you a new cookie"

    # correct password & username
    if stat:
        # create the cookie
        cookie = Cookie.SimpleCookie()
        # set the expire date
        expires = datetime.datetime.utcnow() + datetime.timedelta(days=5)
        cookie['user_name'] = usrname
        cookie['password'] = pwd
        cookie['user_name']['expires'] = expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT")
        cookie['password']['expires'] = expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT")
        data['user_name'] = usrname

    data['result'] = info
    # if cookie has been set
    if cookie:
        print cookie
    print
    print json.dumps(data)

    # print json.dumps(data)

# no cookie, user have to login again during the next visit
else:
    # print "Hello, I won't send you a cookie."
    if stat:
        # create the cookie without expire
        cookie = Cookie.SimpleCookie()
        cookie['user_name'] = usrname
        cookie['password'] = pwd
        data['user_name'] = usrname
        print cookie
    
    data['result'] = info
    print
    print json.dumps(data)

