import psycopg2

# Returns all current fields for a given username and password
# Returns None if the user is not found
def find_user(username, password):
	# Connect to the database
	conn = psycopg2.connect(host="cs346proj2db.ctkh18zy1p4k.us-east-1.rds.amazonaws.com", dbname="cs346proj2db", user="cs346proj2admin", password="proj2pass")
	# Open a cursor to perform database operations
	cur = conn.cursor()

	# Query the database
	cur.execute("SELECT * FROM logins NATURAL JOIN users NATURAL JOIN games NATURAL JOIN rounds WHERE user = %s AND pass = %s;" (username, password))
	response = cur.fetchone()

	# Close communication with the database
	cur.close()
	conn.close()

	return response
