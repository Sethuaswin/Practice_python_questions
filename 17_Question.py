# Question 17:
# Write a Program to accept ‘n’ numbers and store all prime numbers in an array and display the array.

class Prime:
    def check(self, p):
        print("Prime numbers are\n")
        for self.x in p:
            self.flag = 0
            for self.i in range(2, self.x):
                if (self.x % self.i == 0):
                    break
                else:
                    print(self.x)
                    break

list1 = []
n = int(input("Enter how many number you want to insert:\n"))
print("Enter the numbers:\n")
i = 0
while (i < n):
    list1.append(int(input()))
    i = i + 1
s = Prime()
s.check(list1)