
import os
import sys

if (len(sys.argv) != 2):
    print("error: invalid number of arguments")
    print("usage: file_counter.py <path>")
    sys.exit(1)

if (not os.path.isdir(sys.argv[1])):
    print("error: directory not found")
    sys.exit(1)

counter = {}

for directory, directory_names, file_names in os.walk(sys.argv[1]):
    for file_name in file_names:
        ext = os.path.splitext(file_name)[1]
        if not (ext in counter):
            counter[ext] = 1
        else:
            counter[ext] += 1

for file_type, count in sorted(counter.items()):
    if (file_type == ''):
        print("unknown: {}".format(count))
    else:
        print("{}: {}".format(file_type, count))
