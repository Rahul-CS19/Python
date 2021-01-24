# Python program to merge the content of two files
# into the third file

import shutil
file1 = input("Enter the name of file1: ")
file2 = input("Enter the name of file2: ")
Destination = input("Enter the destination filename: ")
with open(Destination, "wb") as wfd:
    for files in(file1, file2):
        with open(files, "rb") as fd:
            shutil.copyfileobj(fd, wfd)
chek = open(Destination, "r")
print(chek.read())
chek.close()
