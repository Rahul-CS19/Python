# Python program to find Occurrence of a character in a string

strl = input("Enter your own String: ")
ch = input("Enter your own character: ")

for i in range (len(strl)):
    if(strl[i] == ch):
        print(ch, "is found at Position", i+1)
