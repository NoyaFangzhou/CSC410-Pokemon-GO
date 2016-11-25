#!/usr/bin/env python

import cgitb
import cgi

cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html"
print

print '''
<html>
  <head>
    <title>Midterm Exam 1</title>
  </head>
  <body>
'''

if form.length <= 0:
    print "No form data received."
else:
    print "Found some form data!<BR/>"
    for key in form:
        print key + " " + form[key].value + "<BR/>"

print '''
  </body>
</head>
'''




