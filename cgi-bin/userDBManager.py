from dbconnector import connect

def query_user(sql_query, username):
	con = connect()
	if con == None:
		return 'Error'
	try:
		with con.cursor() as cursor:
			cursor.execute(sql_query,(username,));
			result = cursor.fetchone()
			con.close()
			return result
	except Exception as e:
		print e
		con.close()
		return 'Error'


def create_user(sql_insert,user_id,encrypted,nickname,salt, email, team):
	con = connect()
	if con == None:
		return 'Error'
	try:
		with con.cursor() as cursor:
			s = cursor.execute(sql_insert,(user_id,encrypted,nickname,salt,email,team));
			con.commit()
			con.close()
			return True
	except Exception as e:
		print 'can not excute the sql command'
		con.close()
		return 'Error'
