import os, sqlite3

def deleteRecord():
    db_path = os.path.join(os.path.dirname(__file__), "SQLite_Python.db")
    try:
        conn = sqlite3.connect(db_path)
        curs = conn.cursor()
        sql_cmd = """DELETE FROM SqliteDb_developers where id = 1"""
        curs.execute(sql_cmd)
        conn.commit()
        curs.close()
    except sqlite3.Error as e:
        print("Deleting record failed. ", e)
        conn.rollback()
    finally:
        if conn:
            conn.close()
            print("Connection to the database is closed.")
    return

def deleteRecordById(Id):
    db_path = os.path.join(os.path.dirname(__file__), "SQLite_Python.db")
    try:
        conn = sqlite3.connect(db_path)
        curs = conn.cursor()
        sql_cmd = """DELETE FROM SqliteDb_developers where id = ?"""
        curs.execute(sql_cmd, (Id,))
        conn.commit()
        curs.close()
    except sqlite3.Error as e:
        print(f"Deleting record by id {Id} failed. ", e)
        conn.rollback()
    finally:
        if conn:
            conn.close()
    return

def deleteMultipleRows(rowList):
    db_path = os.path.join(os.path.dirname(__file__), "SQLite_Python.db")
    try:
        conn = sqlite3.connect(db_path)
        curs = conn.cursor()
        sql_cmd = """DELETE FROM SqliteDb_developers where id = ?"""
        curs.executemany(sql_cmd, rowList)
        conn.commit()
        print("Deleted successfully")
        curs.close()
    except sqlite3.Error as e:
        print("Deleting the rows failed.", e)
        conn.rollback()
    finally:
        if conn:
            conn.close()
            print("Connection to the database is closed.")
    return


rows = [
    (1,),
    (3,),
    (4,),
    (5,),
]
deleteMultipleRows(rows)
rows = [
    (2,),
    (6,),
]
deleteMultipleRows(rows)
