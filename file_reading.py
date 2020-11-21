fp = open("file1.txt", "r")
# print(fp.read()) reads whole file
# content = fp.read(3)
# reads first three character
# print(content)
# print(fp.readline) read one line at a time
# print(fp.readlines()) #reads and display in list
for i in fp:  # reads the whole file
    print(i, end="")
fp.close()
