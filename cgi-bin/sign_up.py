#!C:\Users\nevgivin\Anaconda2\python.exe
import cgi
import cgitb
import database
import datetime
import hashlib


cgitb.enable()

form = cgi.FieldStorage()


print 'Content-Type: text/html'
print

#USER ID
user_id = form['user_id'].value

#USER NICKNAME
nickname = form['nickname'].value

#USER PASSPWORD
password = form['password'].value

#PASSWORD1
re_password = form['re_password'].value

#EMAIL
e_mail = form['email'].value

#TEAM
team = form['team'].value

#SALT
salt = str(datetime.datetime.now())

#ENCRYPTED PASSWORD
hasher = hashlib.md5()
hasher.update(str(password))
hasher.update(salt)
encrypted = hasher.hexdigest()


flag = 0

detect_exist = 'select * from user_account where user_ID = \'%s\''  %user_id

database.create_table(database.create_user_table)
exist = database.query_table(detect_exist)

if exist != None:
	info = 'Sorry, the user_ID has existed , please try another one</br>'
else:
	if re_password != password:
		info = 'Two passwords are not same'
	else:
		sql = 'INSERT INTO user_account (user_ID , password , nickname , salt , email_address , team) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' %(user_id, encrypted, nickname, salt, e_mail, team)
		insert = database.insert(sql)
		if insert == 'Error':
			info = 'An error occur when trying to insert your application to the database'
		else:
			info = 'Congratulations , your account has been created</br>'
			flag = 1

print '''
<html>
    <head>
        <title>Created Account</title>
    </head>
    <body>
        %s</br>
     '''%info
    
if flag == 1:
	print 'You will be redirected to the log_in html'
	print '<meta http-equiv="refresh" content="5;url=../log_in.html">'
else:
	print 'You will be redirected to the index html'
	print '<meta http-equiv="refresh" content="5;url=../index.html">'

print ''' 
    </body>
</html>''' 












#MiniFieldStorage