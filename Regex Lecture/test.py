import re

data = ['software','developer']

text = 'software is a set of instructions'

for pattern in data:
    if re.search(pattern,text):
        print(f"Found match")
    else:
        print("not match")