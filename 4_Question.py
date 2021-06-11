# Question 4:
# Write a  program to accept ‘n’ numbers from user ,
# store these numbers into an array and sort the numbers of an array using function.

# Solution_1
input_value = input("Enter the elements separated by space: ")
input_value = input_value.split()
user_list = [int(i) for i in input_value]
print("Solution_1: ")
print("The sorted list: ",sorted(user_list))

# solution_2
list1 = []
z = True
while z:
    n = int(input("Enter a number: "))
    list1.append(n)
    a = input("Do you want to continue?\n(y/n): ")
    if a != "y":
        z = False
print(f"Solution_2:\nYour list is: {list1}\nSorted list is: {sorted(list1)}")

