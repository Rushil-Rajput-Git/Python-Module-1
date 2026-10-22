print("Enter Marks Obtained in 5 subjects")

Mark1=int(input())
Mark2=int(input())
Mark3=int(input())
Mark4=int(input())
Mark5=int(input())

total= Mark1+ Mark2+Mark3+Mark4+Mark5
avg= int(total/5)

validRange= range (0,101)
if avg not in validRange:
    print("Invalid Input!")

elif avg in range (91, 101):
    print("Your grade is A1")

elif avg in range (81, 91):
    print("Your grade is A2")

elif avg in range (71, 81):
    print("Your geade is B1")

elif avg in range(61, 71):
    print("Your grade is B2")
