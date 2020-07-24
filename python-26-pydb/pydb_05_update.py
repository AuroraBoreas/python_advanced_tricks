import os, sqlite3

def updateOneSalary(new_salary, Id):
    db_path = os.path.join(os.path.dirname(__file__), "SQLite_Python.db")
    try:
        conn = sqlite3.connect(db_path)
        curs = conn.cursor()
        print("Connection to the database succeeded.")
        sql_cmd = """UPDATE SqliteDb_developers set salary = ? where id = ?"""
        curs.execute(sql_cmd, (new_salary, Id))
        conn.commit()
        curs.close()
    except sqlite3.Error as e:
        print("Connection to the database failed.", e)
        conn.rollback()
    finally:
        if conn:
            conn.close()
            print("Connection to the database is closed.")
    return

def updateMany(recordList):
    db_path = os.path.join(os.path.dirname(__file__), "SQLite_Python.db")
    try:
        conn = sqlite3.connect(db_path)
        curs = conn.cursor()
        sql_cmd = """UPDATE SqliteDb_developers set salary = ? where id = ?"""
        curs.executemany(sql_cmd, recordList)
        conn.commit()
        print("Update table successfully.")
        curs.close()
    except sqlite3.Error as e:
        print("Update table failed, ", e)
        conn.rollback()
    finally:
        if conn:
            conn.close()
    return

def updateMultipleColumns(recordList):
    db_path = os.path.join(os.path.dirname(__file__), "SQLite_Python.db")
    try:
        conn = sqlite3.connect(db_path)
        curs = conn.cursor()
        sql_cmd = """UPDATE SqliteDb_developers set email = ?, salary = ? where id = ?"""
        curs.executemany(sql_cmd, recordList)
        conn.commit()
        print("Update table successfully.")
        curs.close()
    except sqlite3.Error as e:
        print("Update table failed.", e)
        conn.rollback()
    finally:
        if conn:
            conn.close()
    return

# updateOneSalary(new_salary=50000, Id=1)
# recordList = [
#     (60000, 1),
#     (10000, 2),
#     (9500, 3),
#     (1010,4),
# ]
# updateMany(recordList)

recordList = [
    ("ZhangLiang@sony.com", 30000, 1),
    ("JoeSarah@sony.com", 10000, 2),
    ("BenEater@gmail.com", 10011, 3),
    ("JonnyTom@gmail.com", 9000, 6),
]
updateMultipleColumns(recordList)