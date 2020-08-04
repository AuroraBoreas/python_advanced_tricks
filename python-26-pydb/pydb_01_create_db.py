import sqlite3

class DBmanager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
    def __enter__(self):
        print("__enter__")
        return self.conn.cursor()
    def __exit__(self, *args):
        print("__exit__")
        self.conn.cursor().close()
        self.conn.close()

db_name = "SQLite_Python.db"
# try:
#     sqliteConnection = sqlite3.connect(db_name)
#     cursor = sqliteConnection.cursor()
#     print("Database created and successfully connected to SQLite")

#     sql_select_query = "Select sqlite_version();"
#     cursor.execute(sql_select_query)
#     record = cursor.fetchall()
#     print("SQLite Database Version is: ", record)
#     cursor.close()
# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if (sqliteConnection):
#         sqliteConnection.close()
#         print("The SQLite connection is closed")

with DBmanager(db_name) as cursor:
    sql_select_query = "Select sqlite_version();"
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
print("SQLite Database Version is: ", records)