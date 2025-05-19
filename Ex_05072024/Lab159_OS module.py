# OS module
# use to interact with the Operating System
# get working dir, change dir, file exist, file name, size file, Environment

import os
import math


print(os.name) # e.g. nt - windows
print(os.getcwd()) # get current working directory

print(math.pi)

# os.chdir(r'd:\Python\PyLearning3xATB\Ex_03072024')
print(os.getcwd()) # get current working directory

print(os.listdir())

# os.mkdir("pramod")

# Why OS module is important?
# Read file, you want to check if exist or not
size = os.path.getsize(r'd:\Python\PyLearning3xATB\Ex_05072024\testdata.txt') 
print(size)

if size != 0:
    print("File exists and has content ")
else:
    print("File does not exist, no content")

# Get modification time
mtime = os.path.getmtime(r'd:\Python\PyLearning3xATB\Ex_05072024\testdata.txt') 
print(mtime) # eporch time

import time
print(time.ctime(mtime))