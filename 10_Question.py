# Question 10:
# Write a program to accept a string from user , delete all vowels from the string and display the result.

# Solution_1:
s = input("Enter Something: ")
vowels = 'aeiou'
for i in s.lower():
    if i in vowels:
        s = s.replace(i,"")
print(f"Solution_1:\nThe Deleted vowels in is: {s}")

#Solution_2:
string1 = str.maketrans(dict.fromkeys("aeiouAEIOU"))
a = input("Enter something: ")
t = a.translate(string1)
print((f"Solution_2:\nThe Deleted vowels in is: {t}"))
