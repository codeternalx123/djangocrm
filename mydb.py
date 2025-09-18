import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="20404057003"
)

# Prepare a cursor object
cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE djangoapp")

print('All Done')