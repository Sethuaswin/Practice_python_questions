# Question 18:
# Write a program to calculate the x to the power y without using Standard functions

# Solution_1:
a = int(input("Enter a = "))
b = int(input("Enter b = "))
c = a**b
print(f"{a}^{b} = {c}")

# Solution_2:
x = int(input("Enter x = "))
y = int(input("Enter y = "))
z = pow(x,y) # syntax for pow(base,expo,mod)
print(f"{x}^{y} = {z}")
