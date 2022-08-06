import re

number_of_barcodes = int(input())
for _ in range(number_of_barcodes):
    data = input()
    pattern = r"(\@{1}\#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(\@{1}\#*)"
    result = re.match(pattern, data)
    if not result:
        print(f"Invalid barcode")
    else:
        extract_numbers = re.findall('\d', result.group())
        if not extract_numbers:
            print(f"Product group: 00")
        else:
            print(f"Product group: {''.join(extract_numbers)}")


