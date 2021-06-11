# Question 16:
# Write a Program to Accept character and display its Ascii value and its Next and Previous Character.

# Solution_1:
a = input("Enter a alphabetic letter: ")
b = ord(a)
b += 1
c = ord(a)
c -=1

print("The ASII value of '"+a+"'is",ord(a))
print(f"The next character of '{a}' is",chr(b))
print(f"The Previous character of '{a}' is",chr(c))

# Solution_2:
class Ltr:
    def Ascii(self,c):
        y=ord(c)
        nex=chr(ord(c)+1)
        pre=chr(ord(c)-1)
        print("{}={} next letter={} prev letter ={}".format(c,y,nex,pre))
l=Ltr()
c=input("enter a character: ")
l.Ascii(c)