import re

pattern = r"(w{3})\.([A-Za-z-0-9]+(\-[A-Za-z-0-9]+)*(\.[a-z]+)+)"
valid_url = []

sentence = input()
while sentence:

    matches = re.search(pattern, sentence)
    if matches:
        valid_url.append(matches.group(0))

    sentence = input()

for element in valid_url:
    print(element)