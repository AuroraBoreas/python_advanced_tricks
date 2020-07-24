import sqlite3

try:
    sqliteConnection = sqlite3.connect("SQLite_Python.db")
    cursor = sqliteConnection.cursor()
    print("Database created and successfully connected to SQLite")

    sqlite_select_query = "Select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")