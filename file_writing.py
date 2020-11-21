# fp = open("NewFile.txt", "w")
# fp.write("This file has been opened in write mode.")
# print("File created successfully!!!")

# print("Content of file is as follow :")
# fp = open("NewFile.txt", "r")
# print(fp.read())

fp = open("NewFile.txt", "a")
itReturns = fp.write("Pragati is writing in it\n")
print(itReturns)
# fp = open("NewFile.txt", "r")
# print(fp.read())

fp.close()
