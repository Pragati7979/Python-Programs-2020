letter = '''Dear <|NAME|> ,
You are selected for the position of CEO 
Date : <|DATE|>'''

name = input("Enter the Name : ")
date = input("Enter the Date : ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
