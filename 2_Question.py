# Question 2:
# Write a   program to accept ‘n’ numbers from user , store these numbers into an array.
# Find out maximum and minimum number from an Array.

# Solution_1

input_value = input("Enter The number separated by space: ")
input_value = input_value.split()
arr = [int(i) for i in input_value]
print('Solution_1: \n')
print("list: ", arr)
print("The Maximum value for given numbers is:", max(arr))
print("The minimum value for given numbers is:", min(arr))

# Solution_2:
list1 = []
z = True
while z:
    n = input("enter a number: ")
    list1.append(n)
    a= input("Do you want to continue (y/n): \n")
    if a != "y":
        z = False
print(f"Solution_2:\n"
      f"The List is: {list1}\nThe Maximum value is: {max(list1)}\nThe Minimum value is: {min(list1)}")