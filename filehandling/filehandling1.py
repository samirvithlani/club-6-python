#file handling..... mode to read and write with file
#r - read
#w - write
#a - append
#r+ - read and write
#w+ - write and read+
#open() - to open a file


file = open("filehandling.txt","a")
file.write("Hello World\n")
file.writelines("Hello World")
file.close()
