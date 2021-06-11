# Question 20:
# Write a program to accept string from the user and replace all occurrences of character ‘a’ by ‘*’ symbol.

# Solution_1:
input_str = input("Enter a sentence: ")
for i in input_str:
    if i in 'a':
        input_str = input_str.replace(i,"*")
print(input_str)

# Solution_2:
input_str1 = input("Enter a sentence: ")
converted = input_str.replace("a",'*')
print(converted)