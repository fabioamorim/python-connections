import pyodbc 

# Create conn
def get_conn_sql():
    server = "DESKTOP-S7MI0CA\SQLEXPRESS"
    database = "teste" # db test
    username = "fabioamorim" # user test
    password = "Adm123456789*" # pass test
    string_conn = "Driver={ODBC Driver 17 for SQL Server};SERVER="+server+";DATABASE="+database+";UID="+username+";PWD="+password

    conn = None 

    try:
        conn = pyodbc.connect(string_conn)
    except pyodbc.Erro as err:
        print(err)

    return conn

# Execute query
def execute_sql(conn, sql, commit=False):

    result = None

    try:
        result = conn.execute(sql)

        if commit:
            conn.commit() 

    except pyodbc.Error as err:
        print(f"{err}\n{sql}")

    return result 

conn = get_conn_sql()

# Create table
def create_table():

    conn = get_conn_sql()

    sql = f"""CREATE TABLE user_login(
            id INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
            login VARCHAR(20) NOT NULL
        )"""

    result = execute_sql(conn, sql, True)

    return result

# Drop table
def drop_table():

    conn = get_conn_sql()

    sql = f"""DROP TABLE IF EXISTS user_login"""

    result = execute_sql(conn, sql, True)

    return result

# Select
def select_table():

    conn = get_conn_sql()

    sql = f"""SELECT * FROM user_login"""

    result = execute_sql(conn, sql)

    return result

# Insert row
def insert_row():

    conn = get_conn_sql()

    sql = f"""INSERT INTO user_login VALUES('foo')"""

    execute_sql(conn, sql, True)

# Delete row
def delete_row():

    conn = get_conn_sql()

    sql = f"""DELETE FROM user_login WHERE id = 4 """

    execute_sql(conn, sql, True)

# Update row
def update_row():

    conn = get_conn_sql()

    sql = f"""UPDATE user_login SET login = 'boo' WHERE id = 5"""

    execute_sql(conn, sql, True)
