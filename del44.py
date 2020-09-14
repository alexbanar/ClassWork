import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='zagadaga369', db='users')
conn.autocommit(True)

# Getting a cursor from dtuhdrthd
cursor = conn.cursor()

# Deleting data into table
cursor.execute("DELETE FROM users.users WHERE name = 'john'")

cursor.close()
conn.close()
