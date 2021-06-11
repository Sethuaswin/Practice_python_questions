# Question 15:
# Write a program to calculate X^(Y+Z)

# Solution_1:
x = int(input("Enter X = "))
y = int(input("Enter Y = "))
z = int(input("Enter Z = "))

a = x**(y+z)

print(f"Solution_1:\n{x}^({y}+{z}) = {a}")

# Solution_2:
def power(a, b, c):
    return a ** (b+c)
X = int(input("Enter X = "))
Y = int(input("Enter Y = "))
Z = int(input("Enter Z = "))

Power = power(X,Y,Z)
print(f"Solution_2: \n{X}^({Y}+{Z}) = {Power}")