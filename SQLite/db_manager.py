import sqlite3
import sqlite3
from sqlite3 import Error


CLIENTQUERY =  """ CREATE TABLE IF NOT EXISTS clients(
            id integer PRIMARY KEY,
            fname text NOT NULL,
            lname text NOT NULL,
            phone_number NUMERIC(10) NOT NULL
            );"""

CARQUERY = """ CREATE TABLE IF NOT EXISTS cars(
            id integer PRIMARY KEY,
            REGISTRAION_NUMBER char(7) NOT NULL,
            MODEL_NAME VARCHAR(25) NOT NULL,
            loc_price NUMBER NOT NULL,
            client_id integer,
            FOREIGN KEY (client_id) REFERENCES clients(id)
            );"""

def create_connection(db_file):
    """" create a database connection to SQLlite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file) # create db connection
        # print(sqlite3.version)
    except Error as e:
        print(e)
    # finally:
    #     if conn:
    #         conn.close() # close the connection
            
    return(conn)

def crete_table(conn, sql_query):
    try:
        c = conn.cursor()
        c.execute(sql_query)
    except Error as e:
        print(e)
        


if __name__ == '__main__':
    # create_connection("pythonsqlite.db") # create the connection 
    connection = create_connection("new_db.db")
    crete_table(connection, CLIENTQUERY)
    crete_table(connection, CARQUERY)