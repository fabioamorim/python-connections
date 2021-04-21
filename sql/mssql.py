import pyodbc 

# Create connection
def get_connection_sql():
    server = "DESKTOP-S7MI0CA\SQLEXPRESS"
    database = "teste" # db test
    username = "fabioamorim" # user test
    password = "Adm123456789*" # pass test
    string_connection = "Driver={ODBC Driver 17 for SQL Server};SERVER="+server+";DATABASE="+database+";UID="+username+";PWD="+password
    
    cnxn = pyodbc.connect(string_connection)
    
    return cnxn

# Execute query
def execute_sql(cnxn, sql, commit=False):

    result = cnxn.execute(sql)

    if commit:
       cnxn.commit() 

    return result 

cnxn = get_connection_sql()

# Create table
def create_table():

    cnxn = get_connection_sql()

    sql = f"""CREATE TABLE user_login(
            id INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
            login VARCHAR(20) NOT NULL
        )"""

    result = execute_sql(cnxn, sql, True)

    return result

# Drop table
def drop_table():

    cnxn = get_connection_sql()

    sql = f"""DROP TABLE IF EXISTS user_login"""

    result = execute_sql(cnxn, sql, True)

    return result

# Select
def select_table():

    cnxn = get_connection_sql()

    sql = f"""SELECT * FROM user_login"""

    result = execute_sql(cnxn, sql)

    return result

# Insert row
def insert_row():

    cnxn = get_connection_sql()

    sql = f"""INSERT INTO user_login VALUES('foo')"""

    execute_sql(cnxn, sql, True)

# Delete row
def delete_row():

    cnxn = get_connection_sql()

    sql = f"""DELETE FROM user_login WHERE id = 4 """

    execute_sql(cnxn, sql, True)

# Update row
def update_row():

    cnxn = get_connection_sql()

    sql = f"""UPDATE user_login SET login = 'boo' WHERE id = 5"""

    execute_sql(cnxn, sql, True)
