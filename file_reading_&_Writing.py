# Reading and writing in the file at the smae time

fp = open("file1.txt", "r+")
print(fp.read())
fp.write("\nThanks for letting me write in you.")
print("You wrote successfully in the file")

print("******* Reading the file after writing in it ********")
fp.seek(0)
print(fp.read())
