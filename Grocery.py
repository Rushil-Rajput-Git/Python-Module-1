from encodings import oem


print("=== GROCERY COST COMPARISON TOOL ===")

rice_price=12
milk_price=4
fruit_price=8
number_of_baskets=2
family_members=4

basket_cost_per_person=((rice_price + milk_price + fruit_price)*number_of_baskets)/ family_members

print("Part 1- Basket Cost Per Person", basket_cost_per_person)

total_items=int(input("Enter Total Items:"))
people=int(input("Enter Number Of People:"))

if people == 0:
    print("You Cannot Share Between 0 People.")

else:
    if total_items % people == 0:
        items_each= total_items // people
        print("They divide equally!")

else:
remainder= total_items % people
print("They do not divide equally! There is a remainder.")

recorded_average=65
total_weeks=4
wrong_week_cost=50
correct_week_cost=80

rebuilt_total= recorded_average- wrong_week_cost + correct_week_cost
corrected_total= rebuilt_total - wrong_week_cost + correct_week_cost
corrected_average= corrected_total / total_weeks

store_a_avarage= 70
store_b_avarage= 75
store_c_avarage= 80
verdict=(corrected_avarage < store_a_avarage) and (corrected_avarage < store_b_avarage, Corrected Average: {corrected_avarage})

print("/n=== SUMMARY ===")
print("Cost Per Person (Part 1):", corrected_avarage)
print("Corrected Weekly Average (Part 3):", corrected_avarage)
print("Is Our Average Cheaper Than All Three Stores?(Part 4):", verdict)