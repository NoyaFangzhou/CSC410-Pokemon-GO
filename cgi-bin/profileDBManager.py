import pymysql
from dbconnector import connect
from datetime import datetime

def update(user_ID , post_data):
	update_sql = 'UPDATE user_account set nickname = %s , email_address = %s where user_ID = %s'

	# print user_ID
	#connect to DB
	con = connect()
	if con == None:
		return 'Error'
	try:
		with con.cursor() as cursor:
			cursor.execute(update_sql,(post_data['nickname'],
									   post_data['email_address'],
									   user_ID
										));
			# print "!!!!!!!!!!!!!!!!!!!!"
			con.commit()
			con.close()
			return True
	except Exception as e:
		print e
		# print "#####################"
		con.close()
		return False

def change_password(user_ID, password , salt):
    
	insert_sql = 'UPDATE user_account SET password = %s , salt = %s where user_ID = %s'


	#connect to DB
	con = connect()
	if con == None:
		return 'Error'
	try:
		with con.cursor() as cursor:
			cursor.execute(insert_sql,(password,salt,user_ID));
			con.commit()
			con.close()
			return True
	except Exception as e:
		print e
		con.close()
		return False


# query_post - retrieve old posts
def query_profile(username):
	#query post ordered by post date
	query_sql = 'SELECT user_ID,email_address,nickname FROM user_account WHERE user_ID = %s'
	results = None
	#connect to DB
	con = connect()
	if con == None:
		return 'Error'
	try:
		with con.cursor(pymysql.cursors.DictCursor) as cursor:
			count = cursor.execute(query_sql,(username));
			con.commit()
			if count > 0:
				results = cursor.fetchall();
				
			con.close()
			return results
	except Exception as e:
		print e
		con.close()
		return None








# def update(user_ID , post_data):
# 	update_sql = 'UPDATE user_account set nickname = %s , email_address = %s where user_ID = %s'
# 	print post_data
# 	#connect to DB
# 	con = connect()
# 	if con == None:
# 		return 'Error'
# 	try:
# 		with con.cursor() as cursor:
# 			cursor.execute(update_sql,(post_data['nickname'],
# 									   post_data['email_address']
# 									   user_ID
# 										));
# 			con.commit()
# 			con.close()
# 			return True
# 	except Exception as e:
# 		print e
# 		con.close()
# 		return False
