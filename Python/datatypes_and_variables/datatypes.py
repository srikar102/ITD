"""
Module: datatypes.py
This module demonstrates Python's built-in data types and their characteristics.
Functions and Operations:
    - range(6): Creates a sequence of numbers from 0 to 5. It's an immutable sequence type that 
      is commonly used in loops. Converting it to a list shows all values: [0, 1, 2, 3, 4, 5].
    - Variable swapping (a, b = b, a + b): Demonstrates tuple unpacking to swap and reassign 
      variables. Uses id() to show memory addresses of integer objects before and after assignment.
Data Types Demonstrated:
    - str: String type used for text data. Immutable sequence of characters. Example: "Hello"
    - int: Integer type for whole numbers without decimal points. Immutable numeric type. Example: 42
    - float: Floating-point type for decimal numbers. Immutable numeric type with precision limits. Example: 3.14
    - bool: Boolean type representing truth values. Only two possible values: True or False. 
      Subclass of int where True == 1 and False == 0.
    - list: Mutable, ordered collection of items. Allows duplicate elements and supports indexing 
      and slicing. Example: [1, 2, 3]
    - tuple: Immutable, ordered collection of items. Cannot be modified after creation. Faster 
      than lists and can be used as dictionary keys. Example: (1, 2, 3)
    - dict: Mutable, unordered collection of key-value pairs. Keys must be unique and hashable. 
      Provides fast lookup. Example: {"name": "John", "age": 30}
    - set: Mutable, unordered collection of unique items. Useful for membership testing and 
      eliminating duplicates. Example: {1, 2, 3}
    - NoneType: Represents the absence of a value. None is a singleton object used as default 
      return value for functions that don't explicitly return anything.
"""

a, b = 0, 1
a, b = b, a + b
print(id(a))
print(id(b)) 
print(type(a))
print(a)
print(b)   

# String
s = "Hello"
print(type(s))

# Integer
i = 42
print(type(i))

# Float
f = 3.14
print(type(f))

# Boolean
bool_val = True
print(type(bool_val))

# List
lst = [1, 2, 3]
print(type(lst))

# Tuple
tpl = (1, 2, 3)
print(type(tpl))

# Dictionary
dct = {"name": "John", "age": 30}
print(type(dct))

# Set
st = {1, 2, 3}
print(type(st))

# NoneType
none_val = None
print(type(none_val))

# range
x = range(6)
print(type(x))
print(list(x))