# Question 14:
# Write a program to accept ‘n’ numbers from user and store these numbers into an array,
# and count the number of occurrences of each number.

# Solution_1:
user_list = input("Enter the element of a list separated by space: ")
user_list = user_list.split()
user_list = [str(i) for i in user_list]
x = input("Enter the number to be counted: ")
occurrences = user_list.count(x)
print(occurrences)

#Solution_2:
from collections import Counter
z = []
x = int(input("Enter how many numbers you want to give: "))
for i in range(x):
    a = int(input("Enter the number: "))
    z.append(a)
x = Counter(z)
print(x)
