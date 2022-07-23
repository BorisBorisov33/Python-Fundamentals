import re

sentence = input()

searched_pattern = r"\b_([A-Za-z0-9]+)\b"
result= re.findall(searched_pattern,sentence)
print(",".join(result))