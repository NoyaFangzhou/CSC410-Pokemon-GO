import pymysql

create_user_table =  'CREATE TABLE IF NOT EXISTS user_account(ID int(255) auto_increment primary key, user_ID varchar(255) ,nickname varchar(255) , password varchar(255), salt varchar(255))'

def  connect():

	try:
		conn = pymysql.connect(host = 'localhost' , user = 'root' , password = 'mysql' , db = 'web_pokemon')
		return conn
	except Exception :
		print 'An error has ocurred when trying to connect to the database' 
		return None



def excute(sql):
	con = connect()
	if con == None:
		return 'Error'
	try:
		with con.cursor() as cursor:
			s = cursor.execute(sql);
			con.commit()
			result = cursor.fetchone()
			con.close()
			return result
	except Exception as e:
		print 'can not excute the sql command'
		con.close()
		return 'Error'
	


def create_table(sql_create_table):
	create_table = excute(sql_create_table)
	if(create_table == 'Error'):
		print 'Can not create the table'
		return

def query_table(sql_query):
	return excute(sql_query)

def insert(sql_insert):
	return excute(sql_insert)
	pass