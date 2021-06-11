# Question 5:<br>
# Write a program to accept customer details such as : Account_no, Name, Balance in Account,
# Assume Maximum 20 Customer In the bank.
# Write a function to print the account no and name of each customer with balance below rs 100.

class Bank_Account:
    def __init__(self,account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def balance_less(self):
        if self.balance < 100:
            return (f"""account no.={self.account_no}
                           name= {self.name}
                           balance= {self.balance}""")


accounts = [Bank_Account(123, "khushboo", 99),
            Bank_Account(124, "harsh", 200),
            Bank_Account(122, "prachi", 88),
            Bank_Account(125, "sanjana", 120)]

for bank in accounts:
    print(bank.balance_less())