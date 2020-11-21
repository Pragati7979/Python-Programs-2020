fp = open("file2.txt", "r+")
fp.write("I love learning new things\nI want to build a huge empire for my family\n& I'will surely have one.")
fp.seek(0)
print(fp.read())

fp.write("\nThanks for listening me, atleast you don't judge me")
print(f"The value of fp.tell is {fp.tell()}")
print("\n********After Writing in the file**********")
fp.seek(0)  # takes you to the starting of the file
print(fp.read())

fp.close()

'''
fp.seek(offset) -->takes you to that postion
fp.tell() --> tells you the current position of the character
'''
