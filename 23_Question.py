# Question 23:
# Write a menu driven program to perform the following operations on string using standard library functions
# - Calculate length of string
# - Reverse a given string
# - Concatenation of one string to another
# - Copy one String into another
# - Compare two string.

z=True
while(z):
    class String:
        def length(self,s):
            print("The length of the string is:\n",len(s))
        def rev(self,s):
            print("The reverse of the string is:\n",s[::-1])
        def con(self,s,s2):
            print("The string after concatenation is:\n",s," ",s2)
        def cop(self,s):
            self.st=s
            print("The string is copied :\n",self.st)
        def comp(self,s,s2):
            if s==s2:
                print("The string is equal")
            else:
                print("The string is not equal")

    sa=String()
    print("\n 1. find the length\n 2. reverse\n 3. concatenate\n 4. copy\n 5. to compare string\n ")
    n=int(input("Enter your choice:\n"))
    if n==1:
        s7=input("Enter a string:\n")
        sa.length(s7)
    elif n==2:
        s1=input("Enter a string:\n")
        sa.rev(s1)
    elif n==3:
        s2=input("Enter a string:\n")
        s3=input("Enter another string:\n")
        sa.con(s2,s3)
    elif n==4:
        s4=input("Enter a string:\n")
        sa.cop(s4)
    elif n==5:
        s5=input("Enter a string:\n")
        s6=input("Enter another string to compare:\n")
        sa.comp(s5,s6)
    c=input("do you want to enter again?(y/n)\n")
    if c!='y':
        z=False
        print("Exited")