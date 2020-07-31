import sqlite3
import os

try:
    os.remove("test.db")
except FileNotFoundError:
    pass

# from sqlite3 import connect
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    print('create table')
    yield
    cur.execute('drop table points')
    print('drop table')

class contextmanager:
    def __init__(self, cur):
        self.cur = cur
    def __enter__(self):
        print('__enter__')
        self.gen = temptable(self.cur)
    def __exit__(self, *args):
        print('__exit__')
        next(self.gen, None)

with sqlite3.connect('test.db') as conn:
    cur = conn.cursor()
    with contextmanager(cur):
        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(2, 1)')
        cur.execute('insert into points (x, y) values(2, 2)')
        for row in cur.execute("select x, y from points"):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)
    