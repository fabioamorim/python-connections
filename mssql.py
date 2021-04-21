import pyodbc 

def get_connection_sql():

    server = "server_name"
    database = "database_name"
    username = "user_name"
    password = "password"
    string_connection = "Driver={ODBC Driver 17 for SQL Server};SERVER="+server+";DATABASE="+database+";UID="+username+";PWD="+password
    cnxn = pyodbc.connect(string_connection)
    
    return cnxn

def execute_sql(cnxn, sql):
    
    result = cnxn.execute(sql)
    return result

cnxn = get_connection_sql()
result = execute_sql(cnxn, "SELECT * FROM user_test")

for row in result:
    print(row)
