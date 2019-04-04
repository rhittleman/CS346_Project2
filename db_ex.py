import psycopg2

# Connect to the database
conn = psycopg2.connect(host="cs346proj2db.ctkh18zy1p4k.us-east-1.rds.amazonaws.com" dbname="cs346proj2db" user="cs346proj2admin" password="proj2pass")

# Open a cursor to perform database operations
cur = conn.cursor()

# Query the database and obtain data as Python objects 
# (tuple of one entry if found, None if not)
cur.execute("SELECT * FROM table;")
cur.fetchone()

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO table (col1, col2) VALUES (%s, %s)", (data1, data2))

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()