#!/usr/bin/env python

# Lecture 08 - jQuery and Ajax

import cgitb
import cgi
import sqlite3

cgitb.enable() # enable debugging output in some cases

print "Content-type: text/html"
print # without printing a blank line, the "end of script output before headers" error will occur
print '''<html>
    <head>
        <title></title>
        <style type="text/css">
        #error {
                color: red
            }
        </style>
    </head>
    <body>'''

form = cgi.FieldStorage()

customer_name = form['customer_name'].value # don't forget the .value

conn = sqlite3.connect('pizza_orders.db')
cursor = conn.cursor()


for order in cursor.execute("SELECT * FROM pizza_orders WHERE name=?", [customer_name]):
    print 'Name: ' + order[0] + "<BR/>"
    print 'Size: ' + order[1] + "<BR/>"
    print 'Crust: ' + order[2] + "<BR/>"
    print 'Toppings: ' + order[3] + "<BR/>"
    print 'Phone Number: ' + order[4] + "<BR/>"
    print 'Credit Card Number: ' + order[5] + "<BR/>"

