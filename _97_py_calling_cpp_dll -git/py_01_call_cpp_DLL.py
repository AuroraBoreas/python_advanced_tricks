import ctypes, os

BASE_DIR = os.path.dirname(__file__)

simple_dll_path = os.path.join(BASE_DIR, r"pkg\SimpleDLL.dll")
simple_dll = ctypes.cdll.LoadLibrary(simple_dll_path)
result1 = simple_dll.add(10, 1)
result2 = simple_dll.sub(10, 1)

print(result1)
print(result2)