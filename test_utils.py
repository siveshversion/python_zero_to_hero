from utils import execute_code
import os
import sqlite3

def test_execution():
    print("Testing Basic Execution...")
    code = "print('Hello Test')"
    output = execute_code(code)
    assert output.strip() == "Hello Test"
    
    print("Testing Error Handling...")
    code_error = "print(1/0)"
    output_error = execute_code(code_error)
    assert "ZeroDivisionError" in output_error

    print("Testing OOP...")
    code_oop = """
class Test:
    def __init__(self):
        self.val = "OOP Works"
t = Test()
print(t.val)
"""
    output_oop = execute_code(code_oop)
    assert "OOP Works" in output_oop.strip()

    print("Testing Modules...")
    code_module = """
import math
print(int(math.sqrt(25)))
"""
    output_module = execute_code(code_module)
    assert "5" in output_module.strip()

    print("Testing File Handling...")
    code_file = """
with open("test_file.txt", "w") as f:
    f.write("File Test")
with open("test_file.txt", "r") as f:
    print(f.read())
"""
    output_file = execute_code(code_file)
    assert "File Test" in output_file.strip()
    
    print("Testing Type Conversion...")
    code_type = """
print(int("10") + 5)
"""
    output_type = execute_code(code_type)
    assert "15" in output_type.strip()

    print("Testing Advanced Functions...")
    code_args = """
def my_func(*args):
    return sum(args)
print(my_func(1, 2, 3))
"""
    output_args = execute_code(code_args)
    assert "6" in output_args.strip()

    print("Testing Inheritance...")
    code_inherit = """
class Parent:
    def say(self):
        print("Parent")
class Child(Parent):
    pass
c = Child()
c.say()
"""
    output_inherit = execute_code(code_inherit)
    assert "Parent" in output_inherit.strip()

    print("Testing Functional Programming...")
    code_func = """
from functools import reduce
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)
total = reduce(lambda x, y: x + y, nums)
print(total)
"""
    output_func = execute_code(code_func)
    assert "[2, 4, 6, 8]" in output_func
    assert "10" in output_func

    print("Testing Mutable vs Immutable...")
    code_mut = """
s = "Hello"
id1 = id(s)
s = s + " World"
id2 = id(s)
print(f"Diff IDs: {id1 != id2}")
"""
    output_mut = execute_code(code_mut)
    assert "Diff IDs: True" in output_mut

    print("Testing Generators...")
    code_gen = """
def gen():
    yield 1
    yield 2
print(list(gen()))
"""
    output_gen = execute_code(code_gen)
    assert "[1, 2]" in output_gen

    print("Testing Decorators...")
    code_dec = """
def dec(f):
    def wrap():
        print("Wrapped")
        f()
    return wrap
@dec
def say():
    print("Hi")
say()
"""
    output_dec = execute_code(code_dec)
    assert "Wrapped" in output_dec

    print("Testing DB (SQLite)...")
    code_db = """
import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('CREATE TABLE t (col text)')
c.execute("INSERT INTO t VALUES ('test')")
conn.commit()
c.execute('SELECT * FROM t')
print(c.fetchone()[0])
"""
    output_db = execute_code(code_db)
    assert "test" in output_db.strip()

    # Clean up
    if os.path.exists("test_file.txt"):
        os.remove("test_file.txt")

if __name__ == "__main__":
    test_execution()
    print("\nAll Phase 1-4 Tests Passed!")
