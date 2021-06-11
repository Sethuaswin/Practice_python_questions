# Question 3:
# Write a menu driven program  that shows the working of a library. The menu option should be
# - ADD BOOK INFORMATION
# - DISPLAY BOOK INFORMATION
# - LIST ALL BOOKS OF GIVEN AUTHOR
# - LIST THE COUNT OF BOOKS IN THE LIBRARY
# - EXIT

database = {}
z = True
while z:
    class Library:
        print("------MENU-----")
        print("1.ADD BOOK INFORMATION\n2.DISPLAY BOOK INFORMATION\n"
              "3.LIST ALL BOOKS OF GIVEN AUTHOR \n4.LIST THE COUNT OF BOOKS IN THE LIBRARY \n"
              "5.EXIT")

        def inputdata(self, author, book):
            database[book] = author
            print("add complete")
        def display(self):
            print(*database, *database.values())
        def liststep(self,author):
            def fill(n):
                if database[n] == author:
                    return True
                else:
                    return False
            res = filter(fill, database)
            for i in res:
                print(i)
        def countbook(self):
            print("total number of book present in library is ", len(database.keys()))

    l = Library()
    ch = input("Enter your choice:\n")
    if ch == '1':
        a = input("Enter the name of author:\n")
        b = input("Enter the book name:\n")
        l.inputdata(a, b)
    elif ch == '2':
        l.display()
    elif ch == '3':
        aut = input("Enter the name of author to list books:\n")
        l.liststep(aut)
    elif ch == '4':
        l.countbook()
    else:
        print("Exited")
    k= input("do want to enter a number(y/n):\n")
    if k != "y":
        z = False