# Question 25:
# Write a program to display whether the input character is a digit or alphabet.

# Solution_1
n = input("Enter your own character: ")
if n.isalpha():
    print(f"The given character {n} is 'Alphabet'")
elif n.isnumeric():
    print(f"The given character {n} is 'Numeric'")
elif n.isspace():
    print(f"The given character {n} is 'Space'")

#Solution_2:
str1 = input("Enter your own character: ")
if 'a' <= str1 <= 'z' or "A" <= str1 <= "Z":
    print(f"The Given character {str1} is 'Alphabet'")
elif '0' <= str1 <= "9":
    print(f"The given character {str1} is 'Numeric'")
else:
    print(f"The given character {str1} is not an Alphabet or Numeric")