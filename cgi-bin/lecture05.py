#!/usr/bin/env python

import cgitb
import datetime
import Cookie
import os

cgitb.enable()
time_string = str(datetime.datetime.now())


# this function prints a blank line (which must follow the header) and then
# prints an HTML message that includes the specified message in the body
def print_html(msg):
    print
    print "<html>"
    print "  <head><title>Lecture 05 Cookie Test</title></head>"
    print "  <body>" + msg + "</body>"
    print "</html>"


# must include at least one header
print "Content-Type: text/html"
# get the stored cookie
stored_cookie_string = os.environ.get('HTTP_COOKIE')

# the client didn't send a cookie
if not stored_cookie_string:
    # make a new cookie and stuff the current time into it
    cookie = Cookie.SimpleCookie()
    cookie['current_time'] = time_string

    # print the cookie as an HTTP Set-Cookie header
    print cookie
    # the printed message includes the cookie timestamp
    message = "<h2>Hello, the current time is: " + cookie['current_time'].value + "</h2>"
    message += "<h1>I am sending a cookie to you!</h1>"
    print_html(message)
# else the client DID send a cookie...
else:
    # get the cookie
    cookie = Cookie.SimpleCookie(stored_cookie_string)
    # start building the message
    message = "<h1>Hello, I received your cookie.</h1>"
    # if it contains the time stamp...
    if 'current_time' in cookie:
        # add it to the message
        message += "<h2>Its saved current time is: " + cookie['current_time'].value + "</h2>"
    # otherwise, we don't understand that cookie...
    else:
        # this is some other cookie and we didn't get what we expected.  print an error message
        message += "<h2>Sorry, I don't understand your cookie.  Looking for 'current_time' but found: </h2>"
        
    # and while we're at it print the contents of the cookie
    for key in cookie:
        message += key + ":" + cookie[key].value + "<BR/>"

    print_html(message)
