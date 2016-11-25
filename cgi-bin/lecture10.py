#!/usr/bin/env python

import cgitb
import cgi
import sqlite3
import hashlib

def authenticate(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    results = conn.execute('SELECT * FROM users WHERE username=?', [username])
    print results
    if results.rowcount == 1: # used to be arraysize!  this is wrong!  Thanks, Jessica!
        row = results.next()
        encrypted = row[1]
        salt = row[2]

        hasher = hashlib.md5()
        hasher.update(password)
        hasher.update(salt)

        digest = hasher.hexdigest()

        conn.close()

        return digest == encrypted
    else:
        return False


cgitb.enable()

login_form = cgi.FieldStorage()

print 'Content-Type: text/html'
print # don't forget required blank line
print '''<html>
    <head>
        <title>Login Results</title>
    </head>
    <body>'''

username = login_form['username'].value
password = login_form['password'].value

if authenticate(username, password):
    print '<h1>User ' + username + ' has been successfully authenticated!</h1>'
else:
    print '<h1>Authentication failed!</h1>'

print '''
    </body>
</html>'''

