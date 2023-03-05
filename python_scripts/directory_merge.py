
import os
import sys

if (len(sys.argv) != 4):
    print("error: invalid number of arguments")
    print("usage: directory_merge.py <path1> <path2> <merge path>")
    sys.exit(1)

if (not os.path.isdir(sys.argv[1])):
    print("error: directory 1 not found")
    sys.exit(1)

if (not os.path.isdir(sys.argv[2])):
    print("error: directory 2 not found")
    sys.exit(1)

if (not os.path.isdir(sys.argv[3])):
    print("error: directory 3 not found")
    sys.exit(1)

dir1 = set()

for directory, directory_names, file_names in os.walk(sys.argv[1]):
    for file_name in file_names:
        dir1.add(file_name)

for directory, directory_names, file_names in os.walk(sys.argv[2]):
    for file_name in file_names:
        if not (file_name in dir1):
            print("xcopy \"{}\\{}\" \"{}\"".format(directory,  file_name, sys.argv[3]))
            if os.system("xcopy \"{}\\{}\" \"{}\"".format(directory,  file_name, sys.argv[3])) != 0:
                print("error")
