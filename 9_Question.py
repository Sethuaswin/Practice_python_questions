# Question 9:
# Write a program to calculate the sum of first digit and last digit of a given number

# Solution_1:
n = input("Enter a number: ")
x = int(n[0]) + int(n[-1])
print(f"The Sum of first and last digit for {n} is: {x}")

#Solution_2:
m = int(input("Enter a Number: "))
Length = len(str(m))
first_dig = m // (10**(Length-1))
Last_dig = m % 10
y = first_dig + Last_dig
print(f"The Sum of first and last digit for {m} is: {y}")