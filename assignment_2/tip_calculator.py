# Teddy Muli Ndaisi         SCT211-0023/2022

print("****Tip Calculator****")
bill = int(input("Enter the bill amount > "))
people = int(input("Enter the number of people splitting the bill > "))
tip_percentage = int(input("Choose the tip percentage (10, 12, 15) > "))
#if ((tip_percentage != 10) or (tip_percentage != 12) or (tip_percentage != 15)):

total_bill = bill + ((tip_percentage/100) * bill)
split_bill = total_bill / people

print(f"Total Bill: {bill}")
print(f"Tip: {(tip_percentage/100) * bill}")
print(f"Total Bill + Tip: {total_bill}")
print(f"Split Bill: {split_bill:.2f}")
print("****Thank you, welcome again****")