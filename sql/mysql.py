from getpass import getpass
from mysql.connector import connect, Error
"""
try:
    with connect(
        host="localhost",
        user="root",
        password=getpass("Enter password: "),
        database="omega_sat_dev"
    ) as connection:
        print(connection)
except Error as e:
    print(e)
"""

mydb = connect(
    host="localhost",
    user="user",
    password="password",
    database = "datebase"
)


mycursor = mydb.cursor()

# Create Databases
# mycursor.execute("CREATE DATABASE dbteste")

# Show all Databases

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
#    print(x)

# Create Table
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Show all tables
#mycursor.execute("SHOW TABLES")

#for x in mycursor:
#    print(x)

# Create table and create attributes 
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Alter table
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")