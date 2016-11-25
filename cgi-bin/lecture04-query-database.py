#!/usr/bin/env python

import cgitb
import cgi
import sqlite3

cgitb.enable()

form = cgi.FieldStorage()


print 'Content-Type: text/html'
print

# should use a query string like the following:
# ?database_name=something.db&table_name=sometable
database_name = form['database_name'].value
table_name = form['table_name'].value

#database_name = 'pizza_orders.db'
#table_name = 'pizza_orders'


print database_name
print table_name

conn = sqlite3.connect(database_name)
c = conn.cursor()

for r in c.execute('select * from ' + table_name + ';'):
    print r
    print "<BR/>"
print

conn.close()


