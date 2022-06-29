def decrease_tax(price_to_decline, years):
    tax_to_decrease = price_to_decline * years
    return tax_to_decrease


def increase_tax(price_to_increase, kilometers_traveled, kilometers_requested):
    ratio = kilometers_traveled // kilometers_requested
    tax_to_increase = price_to_increase * ratio
    return tax_to_increase


vehicles = input().split(">>")

tax_family_car = 50
tax_heavyDuty_car = 80
tax_sports_Car = 100

total_taxes_for_national_agency = 0
for vehicle in vehicles:

    current_vehicle = [vehicle.split(" ")]
    # print(current_vehicle)
    car_type = current_vehicle[0][0]
    car_taxes = int(current_vehicle[0][1])
    car_kilometers = int(current_vehicle[0][2])

    # print(car_kilometers)

    if car_type == "family":
        decreasing_tax = decrease_tax(5, car_taxes)
        increasing_tax = increase_tax(12, car_kilometers, 3000)
        final_tax = tax_family_car + increasing_tax - decreasing_tax
        total_taxes_for_national_agency += final_tax

        print(f"A {car_type} car will pay {final_tax:.2f} euros in taxes.")

    elif car_type == "heavyDuty":
        decreasing_tax = decrease_tax(8, car_taxes)
        increasing_tax = increase_tax(14, car_kilometers, 9000)
        final_tax = tax_heavyDuty_car + increasing_tax - decreasing_tax
        total_taxes_for_national_agency += final_tax

        print(f"A {car_type} car will pay {final_tax:.2f} euros in taxes.")

    elif car_type == "sports":
        decreasing_tax = decrease_tax(9, car_taxes)
        increasing_tax = increase_tax(18, car_kilometers, 2000)
        final_tax = tax_sports_Car + increasing_tax - decreasing_tax
        total_taxes_for_national_agency += final_tax

        print(f"A {car_type} car will pay {final_tax:.2f} euros in taxes.")

    else:
        print(f"Invalid car type.")

print(f"The National Revenue Agency will collect {total_taxes_for_national_agency:.2f} euros in taxes.")
