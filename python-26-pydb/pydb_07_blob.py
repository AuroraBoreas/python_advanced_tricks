import os, sqlite3

def convert_to_bytes(file):
    with open(file, 'rb') as f:
        data = f.read()
    return data

def convert_to_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
    return

def create_table():
    db_path = os.path.join(os.path.dirname(__file__), "blob.db")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql_cmd = """CREATE TABLE employees
                    (id INTEGER  PRIMARY KEY,
                    name TEXT NOT NULL,
                    photo BLOB NOT NULL,
                    resume BLOB NOT NULL);"""
        cursor.execute(sql_cmd)
        conn.commit()
        print("Created table successfully.")
        cursor.close()
    except sqlite3.Error as e:
        print("Creating table failed.", e)
    finally:
        if conn:
            conn.close()
    return

def insertBlob(employeeId, name, picture, resume):
    db_path = os.path.join(os.path.dirname(__file__), "blob.db")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql_cmd = """INSERT INTO employees
                    (id, name, photo, resume)
                    VALUES (?, ?, ?, ?)"""
        employPic = convert_to_bytes(picture)
        employRes = convert_to_bytes(resume)
        record = (employeeId, name, employPic, employRes)
        cursor.execute(sql_cmd, record)
        conn.commit()
        print("Inserted the record successfully.")
        cursor.close()
    except sqlite3.Error as e:
        print("Inserting record failed.", e)
        conn.rollback()
    finally:
        if conn:
            conn.close()
    return

def readBlob():
    db_path = os.path.join(os.path.dirname(__file__), "blob.db")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql_cmd = """SELECT * FROM employees"""
        cursor.execute(sql_cmd)
        for result in cursor.fetchall():
            Id, name, bytesphoto, bytesresume = result
            empphoto_path = os.path.join(os.path.dirname(__file__), f"picture_{Id}_{name}.jfif")
            empres_path = os.path.join(os.path.dirname(__file__), f"resume_{Id}_{name}.jfif")
            convert_to_file(bytesphoto, empphoto_path)
            convert_to_file(bytesresume, empres_path)
            print(f"id:{Id}, name:{name}")
            os.startfile(empphoto_path)
            os.startfile(empres_path)
    except sqlite3.Error as e:
        print("Error occurred.", e)
    finally:
        if conn:
            conn.close()
    return

create_table()
employId = 1
name = 'cat'
picture = os.path.join(os.path.dirname(__file__), r"data\employees\picture.jfif")
resume = os.path.join(os.path.dirname(__file__), r"data\employees\resume.jfif")
insertBlob(employId, name, picture, resume)
readBlob()