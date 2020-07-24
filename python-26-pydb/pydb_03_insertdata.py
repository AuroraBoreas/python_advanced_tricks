import sqlite3, os

def insertVariableIntoTable(_id, name, email, joinDate, salary):
    db_path = os.path.join(os.path.dirname(__file__), "SQLite_Python.db")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        print("Successfully connected to database")
        sql_insert_query = """INSERT INTO SqliteDb_developers
        (id, name, email, joining_date, salary)
        VALUES
        (?, ?, ?, ?, ?)"""
        data_tuple = (_id, name, email, joinDate, salary)
        cursor.execute(sql_insert_query, data_tuple)
        conn.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python Variables into SqliteDb_developers table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")
    return

def insertMultipleRecords(record_list):
    db_path = os.path.join(os.path.dirname(__file__), "SQLite_Python.db")
    try:
        conn = sqlite3.connect(db_path)
        curs = conn.cursor()
        print("Connection to SQLite3 established")
        sql_insert_qry = """INSERT INTO SqliteDb_developers
                        (id, name, email, joining_date, salary)
                        VALUES (?, ?, ?, ?, ?)"""
        curs.executemany(sql_insert_qry, record_list)
        conn.commit()
        print("Total", curs.rowcount, "records inserted into SqliteDb_developers table")
        curs.close()
    except sqlite3.Error as error:
        print("Connection to SQLite3 failed", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")
    return

insertVariableIntoTable(1, 'ZL', 'ZL@sony.com', '2012-12-01', 9000)
insertVariableIntoTable(2, 'Wu Hai', 'Hai.Wu@sony.com', '2011-05-19', 20000)
insertVariableIntoTable(3, 'Ji Wenjian', 'Wenjian.Ji@sony.com', '2012-12-01', 20000)

records = [(4, 'Jos', 'jos@gmail.com', '2019-01-14', 9500),
        (5, 'Chris', 'chris@gmail.com', '2019-05-15',7600),
        (6, 'Jonny', 'jonny@gmail.com', '2019-03-27', 8400)]
insertMultipleRecords(record_list=records)