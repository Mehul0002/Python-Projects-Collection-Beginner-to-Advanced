# Inputs We Need Fro the User 
# total rent
# Total Food  Ordered For The Snacking
# Electricity Units Spend
# Charge Per Unit 
# Person living in Room 
## Output We Need To Calculate
# Total Amount To Be Paid By Each Person


rent  = int(input("Enter Your Hostel flat Rent = "))
food = int (input("Enter  The Amount You Spent On Food = "))
electricity_spend = int(input("Enter The Total Electricity Units Spend = "))
charge_per_unit = int(input("Enter The Charge Per Unit = "))
Persons = int(input("Enter The Total Number Of Persons Living In The Room = "))

total_bill = electricity_spend * charge_per_unit 

Output = (rent + food + total_bill) //  Persons

print("Total Amount To Be Paid By Each Person = ", Output)
