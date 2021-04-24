import psycopg2

# Create connection
def get_connection_sql():
 
    database = "sales"
    user="postgres"
    password="adm123"
    host="127.0.0.1"
    port="5432"

    conn = psycopg2.connect(database=database, user=user, password=password,host=host, port=port)

    return conn 

# Execute query
def execute_sql(conn, sql, commit=False):

    cursor = conn.cursor()
    result = cursor.execute(sql)

    result = None

    if commit:

        conn.commit()
    else:
        result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

# Create table
def create_table():

    conn = get_connection_sql()
    cursor = conn.cursor()

    sql = f"""CREATE TABLE mkt."user_login"
                (
                    id character varying(20) COLLATE pg_catalog."default" NOT NULL,
                    "login" character varying(20) COLLATE pg_catalog."default",
                    CONSTRAINT "user_login_id_pkey" PRIMARY KEY (id)
                ) """
    execute_sql(conn, sql, True)

# Drop table
def drop_table():

    conn = get_connection_sql()
    
    sql = 'DROP TABLE mkt."user_login"'

    execute_sql(conn, sql, True)

# Select table
def select_table():

    conn = get_connection_sql()

    sql = 'SELECT * FROM mkt."TB_VENDEDOR"'

    result = execute_sql(conn, sql)

    for row in result:
        print(row)

# Insert row
def insert_row():

    conn = get_connection_sql()
    login = 'foo'
    sql = f'INSERT INTO mkt."user_login" VALUES(2, \'boo\');'

    execute_sql(conn, sql, True)

# Delete row
def delete_row():
    
    conn = get_connection_sql()
    sql = f'DELETE FROM mkt."user_login" WHERE id = \'1\';' 

    execute_sql(conn, sql, True)  

# Update row
def update_row():

    conn = get_connection_sql()
    sql = 'UPDATE mkt."user_login" SET login = \'boo\' WHERE id = \'2\';'

    execute_sql(conn, sql, True)
