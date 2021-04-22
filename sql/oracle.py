import cx_Oracle

user = 'fabio'
password = '123'
dns_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe')

#Create connection
def get_connection_sql():

    connection = cx_Oracle.connect(f'{user}/{password}@{dns_tns}')
    return connection

# Execute query
def execute_sql(connection, sql, commit=False):

    cursor = connection.cursor()
    cursor.execute(sql)

    result = None

    if commit:

        connection.commit()

    else: 
    
        result = cursor.fetchall()

    cursor.close()
    connection.close()    

    return result

# Create table
def create_table():

    sql = f"""CREATE TABLE user_login_teste(
                id NUMBER CONSTRAINT pk_user_login_teste PRIMARY KEY,
                login VARCHAR2(60) NOT NULL
            )"""

    connection = get_connection_sql()

    execute_sql(connection, sql, True)

# Drop table
def drop_table():

    sql = "DROP TABLE user_login_teste"

    connection = get_connection_sql()

    execute_sql(connection, sql, True)

# Select  
def select_table():

    sql = "SELECT * FROM user_login"

    connection = get_connection_sql()

    result = execute_sql(connection, sql)
        
    for row in result:
        print(row)

# Insert row
def insert_row():

    sql = "INSERT INTO user_login VALUES(5, 'boo')"

    connection = get_connection_sql()

    execute_sql(connection, sql, True)

# Delete row
def delete_row():

    sql = "DELETE FROM user_login WHERE id = 5"

    connection = get_connection_sql()

    execute_sql(connection, sql, True)

# Update row
def update_row():

    sql = "UPDATE user_login SET login = 'user1' WHERE id = 1"

    connection = get_connection_sql()

    execute_sql(connection, sql, True)
