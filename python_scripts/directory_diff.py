
import os
import sys

if (len(sys.argv) != 3):
    print("error: invalid number of arguments")
    print("usage: directory_diff.py <path1> <path2>")
    sys.exit(1)

if (not os.path.isdir(sys.argv[1])):
    print("error: directory 1 not found")
    sys.exit(1)

if (not os.path.isdir(sys.argv[2])):
    print("error: directory 2 not found")
    sys.exit(1)

dir1 = set()
dir2 = set()

for directory, directory_names, file_names in os.walk(sys.argv[1]):
    for file_name in file_names:
        dir1.add(file_name)

for directory, directory_names, file_names in os.walk(sys.argv[2]):
    for file_name in file_names:
        dir2.add(file_name)

for file in dir1:
    if (not (file in dir2)):
        print(file)
