# Question 1:
# Write A program to accept Four digit number from user and count zero , odd and even digits from the entered number

count_zero = 0
count_odd = 0
count_even = 0
user_input = input("Enter a four digit number: ")

for i in user_input:
    i = int(i)
    if i == 0:
        count_zero += 1
    elif i%2 != 0:
        count_odd += 1
    elif i%2 == 0:
        count_even += 1
        
print(f"The Count of zero in {user_input} is: {count_zero} "
      f"\nThe Count of odd in {user_input} is: {count_odd} "
      f"\nThe Count of even in {user_input} is: {count_even}")