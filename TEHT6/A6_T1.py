print ("""Program starting.
       This program can read a file.""")

filename= input("Insert filename:")

print (f'#### START "{filename}" ####')
import os

readfile=open(filename,"r")
while True:
    line= readfile.readline()
    if line == '':
        break
    print(line, end="")
readfile.close()

print (f'#### END "{filename}" ####')

print ("Program ending.")