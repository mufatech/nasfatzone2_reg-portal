import mysql.connector

# Establish connection
connection = mysql.connector.connect(
    # host= 'dpg-csb40qbtq21c7397kmb0-a',
    # user= 'reg_portal_y4v2_user',
    # passwd = 'FlRvFSWjS5BzxDFnjhnp0YoPbRJQnwxd',
    # database= 'reg_portal_y4v2'
    host= 'localhost',
    user= 'mufatech',
    passwd = 'mufatech',
    database= 'nasfat2'
    
)

# Create cursor
cursor = connection.cursor()

# Execute SQL query
cursor.execute("SHOW TABLES")

# Fetch and display results
tables = cursor.fetchall()
for table in tables:
    print(table[0])

# Close the cursor and connection
cursor.close()
connection.close()
