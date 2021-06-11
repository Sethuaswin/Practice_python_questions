# Question 24:
# Write a program to display the multiplication table of a given number.

n = int(input("Enter a number to see multiplication table :"))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")