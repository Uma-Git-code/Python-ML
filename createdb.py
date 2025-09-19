import mysql.connector.cursor
print(1)
try:
    mydb = mysql.connector.connect(
     host='localhost',
     user='root',
     password='mysql2023!@#'
    )
except mysql.connector.Error as err:
    print("SQL not connected")
print(2)

mycursor = mydb.cursor()
print(3)
mycursor.execute("CREATE DATABASE IF NOT EXISTS db_py")
print(4)

