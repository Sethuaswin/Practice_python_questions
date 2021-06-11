# Question 12:
# Write a program to accept a sentence from the user and reverse its each word.

# Solution_1: - It will reverse both sentence and word
input_str = input("Enter something: ")
Reversed = input_str[::-1]
print(f"Your Sentence: {input_str} \nReversed Sentence: {Reversed}")

# Solution_2: - It will reverse only the words not whole sentence
input_str1 = input("Enter something: ")
spaced1 = input_str1.split()
for i in spaced1:
    print("".join(reversed(i)),end=" ")

# Solution_3: - It will reverse the sentence not words
input_str2 = input("\nEnter something: ")
spaced = input_str2.split()
words = reversed(spaced)
reversed_str = " ".join(words)
print(f"Your Sentence: {input_str2} \nReversed Sentence: {reversed_str}")