import mysql.connector
DB=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Mahi@cse140',
)

cursorObject=DB.cursor()
cursorObject.execute("CREATE DATABASE seu")
print("Done")