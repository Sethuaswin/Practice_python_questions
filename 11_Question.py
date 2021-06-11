# Question 11:
# Write a program to accept a string value from the user and accept a char value from the user and and find out
# the total occurrence of char value in the string value.

# Solution_1:
input_str = input("Enter a sentence: ")
to_check = input("Enter the character to be counted: ")
output_str = input_str.count(to_check)
print(f"The Occurrence of '{to_check}' is = {output_str}")

#Solution_2:
def count(s, c):
    res = 0

    for i in range(len(s)):
        if s[i] == c:
            res = res + 1
    return res
str1 = input("Enter a sentence: ")
cunt = input("Enter the character to be counted: ")
print(f"The Occurrence of '{cunt}' is = {count(str1,cunt)}")
