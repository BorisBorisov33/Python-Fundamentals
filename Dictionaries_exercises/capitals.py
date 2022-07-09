countries = input().split(", ")
capitals = input().split(", ")
dictionary_using_zip = dict(zip(countries,capitals))
# dictionary_comprehension = {countries[index]:capitals[index] for index in range(len(countries))}

for country, capital in dictionary_using_zip.items():
    print(f"{country} -> {capital}")