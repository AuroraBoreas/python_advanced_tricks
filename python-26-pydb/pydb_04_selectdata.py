import sqlite3
import os

def readSingleRow(developerId):
    db_path = os.path.join(os.path.dirname(__file__), "SQLite_Python.db") 
    try:
        pass
        # connect to db
        conn = sqlite3.connect(db_path)
        # get cursor
        curs = conn.cursor()
        # display connection successful info
        print("Connection to database succeeded. ")
        # sqlite3 query
        sql_select_qry = """SELECT * FROM SqliteDb_developers where id = ?"""
        curs.execute(sql_select_qry, (developerId,))
        # fetch one row
        onerow = curs.fetchone()
        print(type(onerow), onerow)
        fmt = "{0: <13}: {1}"
        print(fmt.format("Id", onerow[0]))
        print(fmt.format("Name", onerow[1]))
        print(fmt.format("Email", onerow[2]))
        print(fmt.format("JoiningDate", onerow[3]))
        print(fmt.format("Salary", onerow[4]))
        curs.close()
    except sqlite3.Error as e:
        print("Connection to database failed. ", e)
    finally:
        # if sqlite3 is still connecting
        if conn:
            conn.close()
            print("The connection is closed")
    return

def readLimitRows(rowSize):
    db_path = os.path.join(os.path.dirname(__file__), "SQLite_Python.db")
    try:
        conn = sqlite3.connect(db_path)
        curs = conn.cursor()
        sql_cmd = """SELECT * FROM SqliteDb_developers"""
        curs.execute(sql_cmd)
        results = curs.fetchmany(rowSize)
        fmt = "id: {0}, name: {1}, email: {2}, joiningDate: {3}, salary: {4}"
        print("select rows are: ")
        for row in results:
            print(fmt.format(*row))
        curs.close()
    except sqlite3.Error as e:
        print("Connection to database failed.", e)
    finally:
        if conn:
            conn.close()
            print("Connection to database is terminated.")
    return

def readAllRows():
    db_path = os.path.join(os.path.dirname(__file__), "SQLite_Python.db")
    try:
        conn = sqlite3.connect(db_path)
        curs = conn.cursor()
        sql_cmd = """SELECT * FROM SqliteDb_developers"""
        curs.execute(sql_cmd)
        results = curs.fetchall()
        fmt = "id:{0: >3}, name:{1: >10}, email:{2: >20}, joiningdate:{3: >11}, salary:{4: >10}"
        print("Here are all data from table(SQLite_developer) in the database:")
        for result in results:
            print(fmt.format(*result))
        curs.close()
    except sqlite3.Error as e:
        print("Connection to database failed. ", e)
    finally:
        if conn:
            conn.close()
            print("Connection to database is closed")
    return

# readSingleRow(3)
# readLimitRows(3)
readAllRows()