import os, sqlite3

def toTitle(s):
    return str(s).title()

def toLower(s):
    return str(s).upper()

def getEmployeeName(Id):
    db_path = os.path.join(os.path.dirname(__file__), "blob.db")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        conn.create_function("toTitle", 1, toLower)
        sql_cmd = """SELECT toTitle(name) FROM employees WHERE id = ?"""
        cursor.execute(sql_cmd, (Id,))
        name = cursor.fetchone()
        print("name = {0}".format(*name))
        cursor.close()
    except sqlite3.Error as e:
        print("Reading table failed.", e)
    finally:
        if conn:
            conn.close()
    return

getEmployeeName(1)