import re
cities = []

travel_points = 0
text = input()
search_pattern = r"(=|\/)(([A-Z]{1}[A-Za-z]{3,})+)\1"
result = re.findall(search_pattern, text)

for match in re.finditer(search_pattern, text):
    city = match.group(2)
    travel_points += len(city)
    cities.append(city)
print(f'Destinations: {", ".join([str(city) for city in cities])} ')
print(f"Travel Points: {travel_points}")
