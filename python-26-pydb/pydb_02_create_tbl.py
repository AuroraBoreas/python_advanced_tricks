import sqlite3, os

def createTable():
    db_path  = os.path.join(os.path.dirname(__file__), "SQLite_Python.db")
    try:
        sql_conn = sqlite3.connect(db_path)
        cursor   = sql_conn.cursor()
        print("Successfully connected to SQLite")
        sql_create_table_query = """CREATE TABLE SqliteDb_developers (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    email text NOT NULL UNIQUE,
                                    joining_date datetime,
                                    salary REAL NOT NULL);"""
        cursor.execute(sql_create_table_query)
        sql_conn.commit()
        print("SQLite table created")
        cursor.close()
    except sqlite3.Error as error:
        print("Creating the table failed. ", error)
    finally:
        if (sql_conn):
            sql_conn.close()
            print("SQLite connection is closed")
    return