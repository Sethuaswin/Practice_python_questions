# Question 19:
# Write a program to accept three sides of a triangle as input and print whether the Trangle is valid or Not.
# (The trangle is valid, if sum of each of the two sides is greater than the third side.)

# Solution_1
a = int(input("Enter side of triangle a = "))
b = int(input("Enter side of triangle b = "))
c = int(input("Enter side of triangle c = "))

if (a+b)>c and (b+c)>a and (a+c)>b:
    print("Triangle is valid")
else:
    print("Triangle is not valid")

# Solution_2
x = int(input("Enter side of triangle x = "))
y = int(input("Enter side of triangle y = "))
z = int(input("Enter side of triangle z = "))

if (x+y)>z:
    print("Triangle is valid")
elif (y+z)>x:
    print("Triangle is valid")
elif (x+z)>y:
    print("Triangle is valid")
else:
    print("Triangle is not valid")