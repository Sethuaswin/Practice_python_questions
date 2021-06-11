# Question 22:
# Write a program to accept Book Details o f’n’ books as book_title,author, publisher and cost.
# Assign the accession number to each book in increasing order Display these details as .
#
#  - Book s of a specific author
#  - Books by a specific publisher
#  - All Books costing rs 500 and above.
#  - All Books.

database = {}
database1={}
database2={}
z=True
while(z):
    class Library:
        print("------MENU-----")
        print("1.ADD BOOK INFORMATION\n2.DISPLAY BOOK INFORMATION\n3.LIST ALL BOOKS OF GIVEN AUTHOR\n4.LIST ALL BOOKS OF GIVEN PUBLISHER \n5.LIST THE COUNT OF BOOKS IN THE LIBRARY \n6.LIST ALL BOOK BY COST ABOVE 500 \n7.EXIT")
        def inputdata(self,author,book,publisher,cost):
            database[book]=author
            database1[book]=publisher
            database2[book]=cost
            print("add complete")
        def display(self):
            print(*database,*database.values(),*database1.values(),*database2.values())
        def liststep(self,author):
            def fill(n):
                if database[n]==author:
                    return True
                else:
                    return False
            res=filter(fill,database)
            for i in res:
                print(i)
        def liststep1(self,publisher):
            print(database1)
            def fill1(n):
                if database1[n]==publisher:
                    return True
                else:
                    return False
            res1=filter(fill1,database1)
            for j in res1:
                print(j)
        def liststep2(self):
            print(database2)
            def fill2(n):
                if database2[n]>=500:
                    return True
                else:
                    return False
            res2=filter(fill2,database2)
            for k in res2:
                print(k)
        def countbook(self):
            print("total number of book present in library is ",len(database.keys()))
    l=Library()
    ch=input("Enter your choice:\n")
    if ch=='1':
        a=input("Enter the name of author:\n")
        b=input("Enter the book name:\n")
        c=input("Enter the name of publisher:\n")
        d=int(input("Enter the cost of book:\n"))
        l.inputdata(a,b,c,d)
    elif ch=='2':
        l.display()
    elif ch=='3':
        aut=input("Enter the name of author to list books:\n")
        l.liststep(aut)
    elif ch=='4':
        pub=input("Enter the name of publisher to list books:\n")
        l.liststep1(pub)
    elif ch=='5':
        l.countbook()
    elif ch=='6':
            l.liststep2()
    else:
        print("Exited")
    k=input("do want to go to menu?(y/n):\n")
    if k!="y":
        z=False
        print("Exited")