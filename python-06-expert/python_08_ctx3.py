import sqlite3
from contextlib import contextmanager

# from sqlite3 import connect
@contextmanager
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    print('create table')
    try:
        yield
    finally:
        cur.execute('drop table points')
        print('drop table')

with sqlite3.connect('test2.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(2, 1)')
        cur.execute('insert into points (x, y) values(2, 2)')
        for row in cur.execute("select x, y from points"):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)