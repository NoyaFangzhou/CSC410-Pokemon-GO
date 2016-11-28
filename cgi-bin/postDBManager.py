import pymysql
from dbconnector import connect
from datetime import datetime

# insert_post - insert one post into database
# @data: json object, will return to user
# @author: a string of user name
# @post: the post request
# return: true if insert success, false if db error
def insert_post(post_data):

	insert_sql = 'INSERT INTO post (author, content, date, likes) VALUES (%s,%s,%s,%s)'

	#connect to DB
	con = connect()
	if con == None:
		return 'Error'
	try:
		with con.cursor() as cursor:
			cursor.execute(insert_sql,(post_data['author'],
									   post_data['content'],
									   post_data['date'],
									   post_data['likes']));
			con.commit()
			con.close()
			return True
	except Exception as e:
		print e
		con.close()
		return False


# query_post - retrieve old posts
def query_post(username):
	#query post ordered by post date
	query_sql = 'SELECT * FROM post WHERE author = %s ORDER BY date DESC'
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