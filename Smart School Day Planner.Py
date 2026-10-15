print("=== Smart School Day Planner ===")
print("Answer 3 quick questions and I will plan your day!/n")

day= input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather= input("What is the weather like? (Sunny/Rainy/Cloudy): ").strip().lower()
homework= input("Is your homework done? (yes/no):").strip().lower()

print()
print(f"=== Your plan for {day} ===")
print("-" * 35)

if day in ("Saturday", "Sunday"):
    print("Day type   :Weekend- enjoy your free time!")

elif day== "Monday":
    print(" Day Type   :First day of the week. Pack your weekly planner.")

elif day== "Friday":
    print("Day Type :Last school day. Return libary books")

elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day Type :Regular school day. Stay focused!")

else:
    print("Day Type :Day not recognised. Please check spelling")

if weather == "sunny" and homework == "yes":
    print ("After School: Head to park- great weather and homework is done")

if weather == "rainy" or weather =="cloudy":
    print("Weather Tip: Pack your umbrella- it may get wet outside")

if not (homework == "yes"):
    print("Homework: Not done yet. Finish before going out!")