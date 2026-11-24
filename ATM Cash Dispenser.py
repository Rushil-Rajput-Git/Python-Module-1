print ("=== ATM CAash Dispenser ===")
total_100= total_50= total_20= total_10= total_5= total_5= 0
customers_served= 0
total_dispensed= 0

serving= True
while serving:
    name= input("Enter Customer Name:)
    amount= int (input(f"Hello {name}! Enter withdrawl amount:"))
    if amount <= 0:
    print ("Invalid amount! Please enter a positive number!)
    
print(f"/nDispensing {amount} units for {name}")
remaining= amount
idx= 1
while idx <= 6: