"""
Lists and prints all files and directories in the './DevOps' folder.
This script uses the os.listdir() function to retrieve the names of all items
(files and subdirectories) located in the './DevOps' directory relative to the
current working directory. Each item name is then printed to the console on a
separate line.
This is useful for quickly viewing the contents of a directory programmatically.
"""

import os

for name in os.listdir('./DevOps/Python'):
    print(name)