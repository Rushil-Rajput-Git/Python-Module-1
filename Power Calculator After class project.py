print("=== Power Calculator ===")

base= int(input("Enter the base number"))
exponent=int (input("Enter the power"))

result=1
for i in range(1, exponent +1):
    result= result * base
    print("Step", i ":", result)

print(base "To the power of", exponent, "is", result)