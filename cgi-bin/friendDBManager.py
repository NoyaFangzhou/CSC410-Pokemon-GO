import pymysql
from dbconnector import connect
from datetime import datetime



def query_friend(username):
	query_sql = "SELECT user_account1.user_ID AS name, user_account1.team AS team FROM user_account AS user_account1, user_follow , user_account AS user_account2 WHERE user_account2.user_ID = %s AND user_follow.user_follower = user_account2.ID AND user_account1.ID = user_follow.user_followed"
	results = None
	#connect to DB
	con = connect()
	if con == None:
		return 'Error'
	try:
		with con.cursor(pymysql.cursors.DictCursor) as cursor:
			count = cursor.execute(query_sql,(username,));
			if count > 0:
				results = cursor.fetchall();
			con.close()
			return results
	except Exception as e:
		print e
		con.close()
		return 'Error'

def add_follow(username , follow_name):
	
	insert_sql= "INSERT INTO user_follow (user_follower , user_followed)  SELECT user1.ID ,user2.ID FROM user_account user1,user_account user2  WHERE user1.user_ID = %s and user2.user_ID = %s"

	#connect to DB
	con = connect()
	if con == None:
		return False
	try:
		with con.cursor() as cursor:
			cursor.execute(insert_sql,(username , follow_name));
			con.commit()
			con.close()
			return True
	except Exception as e:
		print e
		con.close()
		return False

def delete_follow(username , follow_name):
	delete_sql = "DELETE FROM user_follow WHERE user_follow.user_follower IN (SELECT user_account.ID FROM user_account WHERE user_account.user_ID = %s) AND user_follow.user_followed IN (SELECT user_account.ID FROM user_account WHERE user_account.user_ID = %s)"

	#connect DB
	con = connect()
	if con == None:
		return False
	try:
		with con.cursor() as cursor:
			count = cursor.execute(delete_sql,(username , follow_name));
			con.commit()
			con.close()
			if count > 0:
				return True
			return False
	except Exception as e:
		print e
		con.close()
		return False

def search_user(name):
	search_sql = "SELECT ID,user_ID,team FROM user_account WHERE user_id LIKE %s"
	#connect DB
	con = connect()
	if con == None:
		return False
	try:
		with con.cursor(pymysql.cursors.DictCursor) as cursor:
			count = cursor.execute(search_sql,("%" + name + "%",));
			if count > 0:
				results = cursor.fetchall();
			con.close()
			return results
	except Exception as e:
		print e
		con.close()
		return False


def if_follow(username , friend):
	search_sql = "SELECT * FROM user_follow,user_account as user1, user_account as user2 WHERE user_follow.user_follower = user1.ID and user_follow.user_followed = user2.ID and user1.user_ID = %s and user2.user_ID = %s "
	#connect DB
	con = connect()
	if con == None:
		return False
	try:
		with con.cursor() as cursor:
			count = cursor.execute(search_sql,(username,friend));
			con.close()
			if count > 0:
				return True
			else:
				return False
	except Exception as e:
		print e
		con.close()
		return False


def get_team(username):
	search_sql = "SELECT team from user_account where user_id = %s"

	#connect DB
	con = connect()
	if con == None:
		return False
	try:
		with con.cursor() as cursor:
			cursor.execute(search_sql,(username,));
			result = cursor.fetchone()
			con.close()
			return result
	except Exception as e:
		print e
		con.close()
		return False
		# DELETE FROM user_follow WHERE user_follow.user_follower IN (SELECT user_account.ID FROM user_account WHERE user_account.user_ID = 'x') AND user_follow.user_followed IN (SELECT user_account.ID FROM user_account WHERE user_account.user_ID = 'b')
		# INSERT INTO user_follow (user_follower , user_followed)  SELECT user1.ID ,user2.ID FROM user_account user1,user_account user2  WHERE user1.user_ID = '1' and user2.user_ID = '2';