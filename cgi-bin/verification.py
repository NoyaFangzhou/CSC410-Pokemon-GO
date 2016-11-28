from userDBManager import query_user
import hashlib

def login_verify(username, password):
	#database.create_table(database.create_user_table)

	query = 'select password , salt from user_account where user_ID = %s'
	result = query_user(query, username)
	stat = False
	if result == None:
		info = 'Wrong Username'
	else:
		salt = result[1]
		hasher = hashlib.md5()
		hasher.update(str(password))
		hasher.update(salt)
		encrypted = hasher.hexdigest()
		if encrypted == result[0]:
			info = 'success'
			stat = True
		else:
			info = 'Wrong Password'

	return [stat, info]
