import re
text=input("Enter the text: ")
pattern=input("Enter the pattern to be search: ")
match=re.search(pattern,text)
if match:
    print('Match Found!')
else:
    print('No Match Found!')