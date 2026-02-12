TOPICS = {
    "Introduction": {
        "title": "Welcome to Python Zero to Hero",
        "theory": """
### What is Python?
Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

### Why Python?
*   **Simple Syntax**: Python has a simple syntax similar to the English language.
*   **Versatile**: Used in Web Development, Data Science, AI, Automation, and more.
*   **Large Community**: Huge support and extensive libraries.

### Your First Program
In Python, we use the `print()` function to output text to the screen.

**Try running the code below!**
""",
        "example_code": "print('Hello, World!')\nprint('I am learning Python!')"
    },
    "Variables & Data Types": {
        "title": "Variables & Data Types",
        "theory": """
### Variables
Variables are containers for storing data values. Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.

```python
x = 5
y = "John"
```

### Data Types
Built-in concept of mutable and immutable data types.
*   **Text Type**: `str`
*   **Numeric Types**: `int`, `float`, `complex`
*   **Sequence Types**: `list`, `tuple`, `range`
*   **Mapping Type**: `dict`
*   **Set Types**: `set`, `frozenset`
*   **Boolean Type**: `bool`
*   **Binary Types**: `bytes`, `bytearray`, `memoryview`
""",
        "example_code": """# Integer
x = 10
print(f"x is {x}, type: {type(x)}")

# String
message = "Python is fun"
print(f"message is '{message}', type: {type(message)}")

# Float
pi = 3.14
print(f"pi is {pi}, type: {type(pi)}")

# Boolean
is_awesome = True
print(f"is_awesome is {is_awesome}, type: {type(is_awesome)}")
"""
    },
    "Control Flow": {
        "title": "Control Flow (If/Else & Loops)",
        "theory": """
### If...Else
Python supports the usual logical conditions from mathematics.
*   Equals: `a == b`
*   Not Equals: `a != b`
*   Less than: `a < b`
*   ...and so on.

### While Loops
With the while loop we can execute a set of statements as long as a condition is true.

### For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
""",
        "example_code": """# If/Else
a = 33
b = 200
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# For Loop
fruits = ["apple", "banana", "cherry"]
print("\\nIterating over list:")
for x in fruits:
    print(x)

# Range
print("\\nUsing range():")
for i in range(5):
    print(i)
"""
    },
    "Functions": {
        "title": "Functions",
        "theory": """
### Creating a Function
In Python a function is defined using the `def` keyword.

### Calling a Function
To call a function, use the function name followed by parenthesis.

### Arguments
Information can be passed into functions as arguments.
""",
        "example_code": """def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

def add_numbers(x, y):
    return x + y

result = add_numbers(5, 7)
print(f"5 + 7 = {result}")
"""
    },
    "Data Structures": {
        "title": "Data Structures (Lists & Dicts)",
        "theory": """
### Lists
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data.

### Dictionaries
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
""",
        "example_code": """# List
my_list = ["apple", "banana", "cherry"]
my_list.append("date")
print(f"List: {my_list}")
print(f"First item: {my_list[0]}")

# Dictionary
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"\\nDictionary: {my_dict}")
print(f"Model: {my_dict['model']}")
my_dict["color"] = "red"
print(f"Modified Dict: {my_dict}")
"""
    },
    "OOP Concepts": {
        "title": "Object Oriented Programming (OOP)",
        "theory": """
### Classes and Objects
Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

### The __init__() Function
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties.

### The self Parameter
The `self` parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
""",
        "example_code": """class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old")

p1 = Person("John", 36)
p1.myfunc()

p2 = Person("Alice", 25)
p2.myfunc()
"""
    },
    "Error Handling": {
        "title": "Error Handling (Try/Except)",
        "theory": """
### Try...Except
The `try` block lets you test a block of code for errors.
The `except` block lets you handle the error.
The `else` block lets you execute code when there is no error.
The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

### Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the `try` statement.
""",
        "example_code": """try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
"""
    },
    "List Comprehensions": {
        "title": "List Comprehensions",
        "theory": """
### List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a `for` statement with a conditional test inside.
""",
        "example_code": """fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(f"Old way: {newlist}")

# With List Comprehension
newlist2 = [x for x in fruits if "a" in x]

print(f"New way: {newlist2}")

# Numbers example
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")
"""
    },
    "Modules & Packages": {
        "title": "Modules & Packages",
        "theory": """
### Modules
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.

### Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.
Examples: `math`, `random`, `datetime`, `os`, `sys`
""",
        "example_code": """import math
import random
import datetime

print(f"Pi is approximately {math.pi}")
print(f"Square root of 16 is {math.sqrt(16)}")

random_num = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_num}")

now = datetime.datetime.now()
print(f"Current date and time: {now}")
"""
    },
    "File Handling": {
        "title": "File Handling",
        "theory": """
### File Handling
The key function for working with files in Python is the `open()` function.
The `open()` function takes two parameters; filename, and mode.

### Modes
*   `"r"` - Read - Default value. Opens a file for reading, error if the file does not exist
*   `"a"` - Append - Opens a file for appending, creates the file if it does not exist
*   `"w"` - Write - Opens a file for writing, creates the file if it does not exist
*   `"x"` - Create - Creates the specified file, returns an error if the file exists
*   `"t"` - Text - Default value. Text mode
*   `"b"` - Binary - Binary mode (e.g. images)
""",
        "example_code": """# Write to a file
with open("demo_file.txt", "w") as f:
    f.write("Hello from Python!\\nThis file was created by the app.")

print("Successfully wrote to demo_file.txt")

# Read from the file
print("\\nReading from file:")
try:
    with open("demo_file.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
"""
    },
    "Type Conversion & Strings": {
        "title": "Type Conversion & String Methods",
        "theory": """
### Type Conversion
You can convert from one type to another using `int()`, `float()`, and `str()`.

### String Methods
Strings in Python are arrays of bytes representing unicode characters.
*   `.upper()`: Converts to uppercase
*   `.lower()`: Converts to lowercase
*   `.find()`: Searches the string for a specified value
*   `.replace()`: Replaces a string with another string
*   `in`: Check if a phrase is present in a string
""",
        "example_code": """# Type Conversion
x = 10    # int
y = 3.14  # float
z = "20"  # str converting to int

print(f"Float from int: {float(x)}")
print(f"Int from float: {int(y)}")
print(f"Int from str: {int(z)}")

# String Methods
course = "Python for Beginners"
print(f"Original: {course}")
print(f"Upper: {course.upper()}")
print(f"Find 'for': {course.find('for')}")
print(f"Replace: {course.replace('Beginners', 'Developers')}")
print(f"'Python' in course: {'Python' in course}")
"""
    },
    "Advanced Control Flow": {
        "title": "Advanced Control Flow",
        "theory": """
### Logical Operators
*   `and`: Returns True if both statements are true
*   `or`: Returns True if one of the statements is true
*   `not`: Reverse the result

### Ternary Operator
A one-line shorthand for an if-else statement.
`value_if_true if condition else value_if_false`

### Nested Loops
A loop inside another loop. The "inner loop" will be executed one time for each iteration of the "outer loop".
""",
        "example_code": """# Logical Operators
income = 50000
has_credit = True

if income > 30000 and has_credit:
    print("Eligible for loan")

# Ternary Operator
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(f"Status: {message}")

# Nested Loops (Coordinates)
print("Coordinates:")
for x in range(2):
    for y in range(2):
        print(f"({x}, {y})")
"""
    },
    "Advanced Functions": {
        "title": "Advanced Functions",
        "theory": """
### *args
If you do not know how many arguments that will be passed into your function, add a `*` before the parameter name.
This way the function will receive a tuple of arguments.

### **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisks: `**` before the parameter name.
This way the function will receive a dictionary of arguments.
""",
        "example_code": """# *args
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum: {sum_all(10, 20, 30, 40)}")

# **kwargs
def save_user(**user):
    print(f"User: {user}")
    print(f"Name: {user['name']}")

save_user(id=1, name="John", admin=True)
"""
    },
    "OOP Inheritance": {
        "title": "OOP Inheritance",
        "theory": """
### Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

*   **Parent class**: The class being inherited from, also called base class.
*   **Child class**: The class that inherits from another class, also called derived class.

### super()
The `super()` function is used to give access to methods and properties of a parent or sibling class.
It is commonly used in `__init__` to ensure the parent is initialized correctly.
""",
        "example_code": """class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a generic sound")

class Dog(Animal):
    def __init__(self, name, breed):
        # Call Parent's __init__ using super()
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # Call Parent's speak using super()
        super().speak()
        print(f"{self.name} ({self.breed}) says: Woof!")

d = Dog("Buddy", "Golden Retriever")
d.speak()

print("-" * 20)

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

c = Cat("Whiskers")
c.speak()
"""
    },
    "Functional Programming": {
        "title": "Functional Programming",
        "theory": """
### Lambda Functions
A small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
Syntax: `lambda arguments : expression`

### Map
The `map()` function executes a specified function for each item in an iterable.
The item is sent to the function as a parameter.

### Filter
The `filter()` function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

### Reduce
The `reduce()` function applies a rolling computation to sequential pairs of values in a list.
Must be imported from `functools`.
""",
        "example_code": """from functools import reduce

# Lambda
add = lambda a, b: a + b
print(f"Lambda add: {add(5, 6)}")

# Map
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(f"Map doubled: {doubled}")

# Filter
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Filter evens: {evens}")

# Reduce
total = reduce(lambda x, y: x + y, nums)
print(f"Reduce total: {total}")
"""
    },
    "Mutable vs Immutable": {
        "title": "Mutable vs Immutable",
        "theory": """
### Immutable Types
An immutable object is an object whose state cannot be modified after it is created.
Examples: `int`, `float`, `bool`, `str`, `tuple`, `frozenset`.
Reassigning a variable does NOT modify the object; it points the variable to a new object.

### Mutable Types
A mutable object is an object whose state can be modified after it is created.
Examples: `list`, `dict`, `set`, `bytearray`.
Modifying the object keeps the same memory address (identity).

### id() Function
You can use `id(object)` to check the unique identifier (memory address) of an object.
""",
        "example_code": """# Immutable Example (String)
s = "Hello"
print(f"Original String: {s}, ID: {id(s)}")
s = s + " World"
print(f"New String:      {s}, ID: {id(s)}")
print("Notice the ID changed! A new object was created.\\n")

# Mutable Example (List)
lst = [1, 2, 3]
print(f"Original List: {lst}, ID: {id(lst)}")
lst.append(4)
print(f"Modified List: {lst}, ID: {id(lst)}")
print("Notice the ID stayed the same! The object was modified in place.")
"""
    },
    "Python Architecture & Scope": {
        "title": "Python Architecture & Variable Scope",
        "theory": """
### Python Architecture
1.  **Source Code (.py)**: The code you write.
2.  **Bytecode (.pyc)**: Python compiles source code to bytecode (low-level, platform-independent).
3.  **PVM (Python Virtual Machine)**: Executes the bytecode line by line.

### Variable Scope (LEGB Rule)
*   **Local**: Variables strictly inside a function.
*   **Enclosing**: Variables in the local scope of enclosing functions (nested functions).
*   **Global**: Variables defined at the top level of a module.
*   **Built-in**: Preassigned in Python (e.g., `open`, `range`).

Use the `global` keyword to modify a global variable inside a function.
""",
        "example_code": """x = "Global"

def my_func():
    x = "Local"
    print(f"Inside function: {x}")

my_func()
print(f"Outside function: {x}")

def modify_global():
    global x
    x = "Modified Global"

modify_global()
print(f"After modify_global: {x}")
"""
    },
    "PEP 8 & Best Practices": {
        "title": "PEP 8 & Best Practices",
        "theory": """
### What is PEP 8?
PEP 8 is the style guide for Python code. It ensures consistency and readability.

### Key Guidelines
*   **Indentation**: Use 4 spaces per indentation level.
*   **Line Length**: Limit all lines to a maximum of 79 characters.
*   **Imports**: Imports should be on separate lines and at the top of the file.
*   **Whitespace**: Avoid extraneous whitespace in the following situations.
*   **Naming Conventions**:
    *   `variable_name`, `function_name` (snake_case)
    *   `ClassName` (CamelCase)
    *   `CONSTANTS` (UPPER_CASE)
""",
        "example_code": """# Good PEP 8 Style
import math

class CircleCalculator:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.PI * (self.radius ** 2)

c = CircleCalculator(5)
print(f"Area: {c.calculate_area()}")
"""
    },
    "Advanced OOP": {
        "title": "Advanced Object Oriented Programming",
        "theory": """
### Encapsulation & Access Specifiers
*   **Public**: Accessible from anywhere (e.g., `self.name`).
*   **Protected**: Accessible within class and subclasses (`_name`). Convention only.
*   **Private**: Accessible only within the class (`__name`). Python mangles the name.

### Polymorphism
Polymorphism allows different classes to be treated as instances of the same general class through key methods.

### Abstraction
Hiding complex implementation details and showing only the necessary features of an object.
Use `abc` module to define Abstract Base Classes.

### Class vs Static Methods
*   **@classmethod**: Takes `cls` as first argument. Can allow access to class state.
*   **@staticmethod**: No implicit first argument. Behaves like a regular function but belongs to the class namespace.
""",
        "example_code": """from abc import ABC, abstractmethod

# Abstraction
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Inheritance & Polymorphism
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

# Class/Static Methods
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_valid(x):
        return x > 0

# Testing
rect = Rectangle(10, 20)
print(f"Rectangle Area: {rect.area()}")

acc = BankAccount(100)
acc.deposit(50)
print(f"Balance: {acc.get_balance()}")
# print(acc.__balance) # AttributeError

print(f"Instance Count: {MyClass.get_count()}")
"""
    },
    "Advanced Functional Patterns": {
        "title": "Advanced Functional Patterns",
        "theory": """
### Generators & Yield
Generators are simple ways to create iterators. They use the `yield` keyword to return data one at a time, saving memory.

### Decorators
Decorators allow you to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

### Recursion
A recursive function is a function that calls itself. Useful for tasks like tree traversal or factorial calculation.

### Closures
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

### Partial Functions
Partial functions allow you to fix a certain number of arguments of a function and generate a new function.
""",
        "example_code": """# Generator
def my_gen():
    yield 1
    yield 2
    yield 3

print(list(my_gen()))

# Recursive Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(f"Factorial of 5: {factorial(5)}")

# Decorator
def my_decorator(func):
    def wrapper():
        print("Something before function.")
        func()
        print("Something after function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Closure
def outer(msg):
    def inner():
        print(msg) # Remembers 'msg'
    return inner

hi_func = outer("Hi Closure")
hi_func()
"""
    },
    "Libraries & Practical Skills": {
        "title": "Libraries & Practical Skills",
        "theory": """
### Database (SQLite)
Python comes with a lightweight relational database called SQLite.
We interact with it using the `sqlite3` module.

### Logging
Better than `print()`. Use `logging` to track events in code.
Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.

### Data Analysis (Pandas)
Pandas is a powerhouse for data manipulation. The core structure is a `DataFrame` (table).

### Visualization (Matplotlib)
Matplotlib is used for plotting graphs.
(Note: In this interactive environment, we simulate the output).

### Web Frameworks
*   **Flask/Django**: For building full-featured web sites.
*   **Streamlit**: For data apps (like this one!).
""",
        "example_code": """import sqlite3
import pandas as pd
import logging

# Database
conn = sqlite3.connect(':memory:') # RAM DB
c = conn.cursor()
c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
c.execute("INSERT INTO stocks VALUES ('2023-01-05','BUY','RHAT',100,35.14)")
conn.commit()

c.execute('SELECT * FROM stocks')
print(f"DB Row: {c.fetchone()}")

# Logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
logging.warning("This is a warning!")

# Pandas
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(f"\\nPandas DataFrame:\\n{df}")
"""
    }
}
