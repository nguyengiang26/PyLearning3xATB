# Walk in DIR: what exactly are the root/current dir, sub dir, how may file
import os
for root, dirs, files in os.walk(r'd:\Python\PyLearning3xATB\Ex_05072024'):
    print("Root:", root)
    print("Directories:", dirs)
    print("Files:", files)
    print("*"*20)
    


