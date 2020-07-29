# to deal with non-decodable characters,
# Unix like system using surrogateescape approach
# WinOS system using strict approach
import os, pprint
a = os.listdir('.')
# pprint.pprint(a)
file_name_bytes = [f for f in os.listdir(b'.') if not f.startswith(b'fpy_') and not f.startswith(b'.vs')]
# print(file_name_bytes)
for f in file_name_bytes:
    oni_handler_unix = 'surrogateescape'
    oni_handler_win = 'strict'
    try:
        print(format("decoding:{}".format(oni_handler_win), "-^20"))
        py_name_str = f.decode('ascii', oni_handler_win)
        print(py_name_str)
        py_name_bytes2 = py_name_str.encode('ascii', oni_handler_win)
        print(py_name_bytes2)
    except UnicodeDecodeError:
        print(format("decoding:{}".format(oni_handler_unix), "-^20"))
        py_name_str = f.decode('ascii', oni_handler_unix)
        print(py_name_str)
        py_name_bytes2 = py_name_str.encode('ascii', oni_handler_unix)
        print(py_name_bytes2)