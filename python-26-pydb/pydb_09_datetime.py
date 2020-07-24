import os, sqlite3
import datetime

def addDeveloper(Id, name, joinDate):
    db_path = os.path.join(os.path.dirname(__file__), "blob.db")
    try:
        conn = sqlite3.connect(db_path, detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()
        # create a table
        sql_cmd_create = """CREATE TABLE new_developers
                     (id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     joinDate TIMESTAMP NOT NULL);"""
        cursor.execute(sql_cmd_create)
        conn.commit()
        print("Created new_developers table successfully.")
        # insert a row into the table
        sql_cmd_insert = """INSERT INTO new_developers
                            (id, name, joinDate)
                            VALUES
                            (?, ?, ?);"""
        record = (Id, name, joinDate)
        cursor.execute(sql_cmd_insert, record)
        conn.commit()
        print("Inserted a row into new_developers table successfully.")
        # fetch a row from the table
        sql_cmd_read = """SELECT * FROM new_developers WHERE id = ?"""
        cursor.execute(sql_cmd_read, (Id,))
        result = cursor.fetchone()
        print("id={0}, name={1}, joinDate={2}".format(*result))
        cursor.close()
    except sqlite3.Error as e:
        print("Creating table failed. ", e)
        conn.rollback()
    finally:
        if conn:
            conn.close()
    return

addDeveloper(1, "Meow", datetime.datetime.now())