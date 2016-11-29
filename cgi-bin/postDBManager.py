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
		return False, 0
	try:
		with con.cursor() as cursor:
			cursor.execute(insert_sql,(post_data['author'],
									   post_data['content'],
									   post_data['date'],
									   post_data['likes']));
			post_id = cursor.lastrowid
			con.commit()
			con.close()
			return True, post_id
	except Exception as e:
		print e
		con.close()
		return False, 0


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
			count = cursor.execute(query_sql,(username,));
			if count > 0:
				results = cursor.fetchall();
				
			con.close()
			return results
	except Exception as e:
		print e
		con.close()
		return 'Error'

# delete_post - delete one post by id
def delete_post(post_id):
	#query sql
	delete_sql = 'DELETE FROM post WHERE id = %s'
	#connect DB
	con = connect()
	if con == None:
		return False
	try:
		with con.cursor() as cursor:
			count = cursor.execute(delete_sql,(int(post_id),));
			con.commit()
			con.close()
			if count == 1:
				return True
			return False
	except Exception as e:
		print e
		con.close()
		return False

# do_like - add 1 on like records by post id 
def do_like(post_id):
	#query the post
	query_sql = 'SELECT likes FROM post WHERE id = %s'
	#update method
	update_sql = 'UPDATE post SET likes = %s WHERE id = %s'
	#connect DB
	con = connect()
	if con == None:
		return False
	try:
		with con.cursor() as cursor:
			count = cursor.execute(query_sql,(int(post_id),));
			if count == 1:
				result = cursor.fetchone();
			else:
				con.close()
				return False

			new_likes = result[0]
			new_likes += 1
			count = cursor.execute(update_sql,(new_likes,int(post_id)));
			con.commit()
			con.close()
			if count == 1:
				return True

			return False

	except Exception as e:
		print e
		con.close()
		return False
	