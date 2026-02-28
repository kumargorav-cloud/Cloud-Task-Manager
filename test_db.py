import psycopg2

try:
	conn = psycopg2.connect(
		dbname='taskdb',
		user='taskuser',
		password='StrongPassword123',
		host='localhost'
	)
	print("Database connection successful!")
	conn.close()

except Exception as e:
	print("Error:",e)
