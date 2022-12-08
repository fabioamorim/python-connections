import cx_Oracle

user = 'fabio'
password = '123'
dns_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe')

#Create conn
def get_conn_sql():

    conn = None

    try:
        conn = cx_Oracle.connect(f'{user}/{password}@{dns_tns}')
    except cx_Oracle.Error as err:
        print(f"{err}")

    return conn

# Execute query
def execute_sql(conn, sql, commit=False):

    result = None
    cursor = conn.cursor()

    try:
        cursor.execute(sql)

        if commit:
            conn.commit()
        else: 
            result = cursor.fetchall()

    except cx_Oracle.Error as err:
        print(f"{err}\nSQL: {sql}")        
           

    cursor.close()
    conn.close()    

    return result

# Create table
def create_table():

    sql = f"""CREATE TABLE user_login_teste(
                id NUMBER CONSTRAINT pk_user_login_teste PRIMARY KEY,
                login VARCHAR2(60) NOT NULL
            )"""

    conn = get_conn_sql()

    execute_sql(conn, sql, True)

# Drop table
def drop_table():

    sql = "DROP TABLE user_login_teste"

    conn = get_conn_sql()

    execute_sql(conn, sql, True)

# Select  
def select_table(sql):

    result = None

    conn = get_conn_sql()

    if(conn is not None):
        result = execute_sql(conn, sql)

        if(result is not None):
            for row in result:
                print(row)

# Insert row
def insert_row():

    sql = "INSERT INTO user_login VALUES(5, 'boo')"

    conn = get_conn_sql()

    execute_sql(conn, sql, True)

# Delete row
def delete_row():

    sql = "DELETE FROM user_login WHERE id = 5"

    conn = get_conn_sql()

    execute_sql(conn, sql, True)

# Update row
def update_row():

    sql = "UPDATE user_login SET login = 'user1' WHERE id = 1"

    conn = get_conn_sql()

    execute_sql(conn, sql, True)

select_table("SELECT * FROM user_login")