import os
print("Operating System:",os.name)
#
print("\nCurrent Working Directory: ",os.getcwd())
print("\nList of files and directories in the current directory:")
print(os.listdir('.'))
print("\nTest if a specified file exis or not:")
try:
     filename = "abc.txt"
     f = open(filename, 'r')
     txt=f.read()
     print(txt)
     f.close()
except IOError:
    print("Not accessed or problem in reading:" +filename)
    