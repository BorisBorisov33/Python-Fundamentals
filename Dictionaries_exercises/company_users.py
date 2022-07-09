companies = {}
command = input().split(" -> ")
while command[0] != "End":
    company, company_id = command

    if company in companies.keys():
        if company_id not in companies[company]:
            companies[company].append(company_id)
    else:
        companies[company] = []
        companies[company].append(company_id)

    command = input().split(" -> ")

for company in companies.keys():
    print(f"{company}")
    for employee in companies[company]:  # companies[company]
        print(f"-- {employee}")
