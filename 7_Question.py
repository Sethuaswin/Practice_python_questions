# Question 7:
# Write a program to calculate the sum of digits of a given number.

n = int(input("Enter a number: "))
x = 0
while n>0:
    dig = n%10
    x = x + dig
    n = n//10
print(f"The sum of digits of given number is: ",x)