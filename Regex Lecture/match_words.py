import re

txt = input()
search_pattern = r'\b([A-Z][a-z]+ [A-Z][a-z]+)\b'

result = re.findall(search_pattern, txt)
formatted_print = " ".join(result)
print(formatted_print)
