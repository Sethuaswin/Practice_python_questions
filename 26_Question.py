# Question 26:
# Write a program to accept basic salary from user.
# If basic salary>=5000 then,
# hra=15% and da=150% of basic salary.
# If basic salary<5000 then,
# hra=10% and da=110% of basic salary
# Display the Gross salary.

basic_salary = float(input("Enter your basic salary: "))
if basic_salary >= 5000:
    HRA = round((0.15 * basic_salary),3)
    DA = round((1.5 * basic_salary),3)
elif basic_salary < 5000:
    HRA = round((0.1 * basic_salary),3)
    DA = round((1.1 * basic_salary),3)

Gross_salary = round((basic_salary + HRA + DA),3)

print(f"\nYour Basic Salary : {basic_salary}\nYour HRA: {HRA}\nYour DA: {DA}\nYour Gross salary: {Gross_salary}")