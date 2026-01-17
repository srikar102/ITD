# LIST BASICS
"""
LIST BASICS AND OPERATIONS
This module provides a comprehensive introduction to Python lists, covering:
- List Creation: Multiple ways to instantiate lists (empty lists, populated lists,
    mixed-type lists, and nested lists)
- Accessing Elements: Methods for retrieving list items using positive/negative
    indexing and slicing notation to extract subsets of the list
- Modifying Lists: Operations to change list contents including element replacement,
    appending, inserting at specific positions, extending with multiple items,
    and removing elements by value or index
- List Methods: Built-in methods for list manipulation such as sorting,
    reversing, counting occurrences, finding indices, and creating shallow copies
- Iteration: Techniques for traversing lists including basic for loops and
    enumerate() for accessing both index and value simultaneously
- List Comprehension: Concise syntax for creating new lists by applying
    transformations or filters to existing sequences
- Membership Testing: Checking list length and verifying element existence
    using the 'in' operator
Key Concepts:
- Lists are ordered, mutable (changeable) collections
- They support heterogeneous data types (multiple types in one list)
- Indexing is zero-based with support for negative indices (counting from end)
- In-place modifications affect the original list
- List comprehensions provide efficient, readable list creation
"""
# Lists are ordered, mutable collections that can hold multiple items

# Creating lists
empty_list = [] # empty list
empty_list2 = list() # another way to create an empty list
fruits = ["apple", "banana", "cherry"] # list of strings
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

# ACCESSING ELEMENTS
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])      # apple (first element)
print(fruits[-1])     # date (last element)
print(fruits[1:3])    # ["banana", "cherry"] (slicing)

# MODIFYING LISTS
fruits[0] = "apricot"  # change element
fruits.append("elderberry")  # add at end
fruits.insert(1, "blueberry")  # add at position
fruits.extend([1, 2, 3])  # add multiple items
fruits.remove("apple")  # remove by value
removed = fruits.pop()  # remove last item
fruits.pop(0)  # remove by index

# LIST METHODS
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()  # sort in place
numbers.reverse()  # reverse in place
count = numbers.count(1)  # count occurrences
index = numbers.index(4)  # find index of value
copy = numbers.copy()  # shallow copy

# ITERATION
for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# LIST COMPREHENSION
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# LENGTH & MEMBERSHIP
print(len(fruits))  # number of items
print("apple" in fruits)  # True/False