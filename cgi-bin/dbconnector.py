import pymysql

dbpass = '931119ma'
dbuser = 'root'
dbhost = 'localhost'
dbname = 'web_pokemon'

def  connect():

	try:
		conn = pymysql.connect(host = dbhost , user = dbuser , password = dbpass , db = dbname)
		return conn
	except Exception :
		print 'An error has ocurred when trying to connect to the database' 
		return None