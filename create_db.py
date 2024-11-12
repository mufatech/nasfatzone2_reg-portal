import mysql.connector

mydb = mysql.connector.connect(
    # host= 'dpg-csb40qbtq21c7397kmb0-a',
    # user= 'reg_portal_y4v2_user',
    # passwd = 'FlRvFSWjS5BzxDFnjhnp0YoPbRJQnwxd',
    # host= 'aws-0-us-west-1',
    # user= 'reg_portal_y4v2_user',
    # passwd = 'FlRvFSWjS5BzxDFnjhnp0YoPbRJQnwxd',
    host= 'localhost',
    user= 'mufatech',
    passwd = 'mufatech',
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE nasfat2")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)