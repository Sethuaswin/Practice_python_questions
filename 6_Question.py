# Question 6:
# Write a program to accept 5 names from user and store these names into an array,
# sort these array element in alphabetical order.

# Solution_1:
list1 = []
z = True
while z:
    n = input("Enter a name: ")
    list1.append(n)
    a = input("Do You Want To Continue?\n(y/n):")
    if a!= 'y':
        z = False
print(f"Solution_1:\nYour list of name: {list1}\nSorted list: {sorted(list1)}")

# Solution_2:
input_name = input("\nEnter a names separated by space: \n")
input_name = input_name.split()
name_list = [str(i) for i in input_name]
print(f"Solution_2:\nYour list is: {name_list}\nSorted list is: {sorted(name_list)}")