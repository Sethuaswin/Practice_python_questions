'''
Question 13:
Write a program to calculate sum of elements of M*N matrix.
'''

# solution_1
import numpy as np
arr1 = np.array([[1,2,3],
                [4,5,6]])
x = np.sum(arr1)
print("The Sum of all the element in given matrix is:",x)

# Solution_2:
m = int(input("Enter the number of rows in the matrix (m): "))
n = int(input("Enter the number of rows in the matrix (n): "))
s = 0
print(f"The Size of the matrix is: {m}X{n}")
for i in range(0,m):
    for j in range(0,n):
        print("Enter: ",i,",",j)
        a = int(input("Enter a value: "))
        s = s + a
print("The Sum of all the element in given matrix is: ",s)
