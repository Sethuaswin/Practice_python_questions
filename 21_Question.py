# Question 21:
# Write a program to create student structure having fields roll_no, stud_name, mark1, mark2,mark3.
# Calculate the total and average of marks and arrange the records in descending order of marks.

# Solution_1
list1 = []
list2 = []
student = int(input("How many student details to be entered?\n"))
for i in range(student):
    student_name = input("Enter student name: ")
    list1.append(student_name)
    roll_no = input("Enter student roll no: ")
    list1.append(roll_no)
    mark1 = int(input("Enter mark_1: "))
    list2.append(mark1)
    mark2 = int(input("Enter Mark_2: "))
    list2.append(mark2)
    mark3 = int(input("Enter Mark_3: "))
    list2.append(mark3)
    total_marks = mark1+mark2+mark3
    print('The total marks of the student is: ',total_marks)
    average_marks = total_marks/3
    print('The average marks of the student is: ', round(average_marks,3))
list2.sort(reverse=True)
print("The descending of the marks is: \n",list2)
print("The student information is: \n",list1)

# Solution_2:
class Student_structure:
    def __init__(self,roll_no,stud_name,mark_1,mark_2,mark_3):
        self.roll_no = roll_no
        self.stud_name = stud_name
        self.mark_1 = mark_1
        self.mark_2 = mark_2
        self.mark_3 = mark_3

    def total(self):
        return (self.mark_1+self.mark_2+self.mark_3)
    def average(self):
        return ((self.mark_1+self.mark_2+self.mark_3)/3)
    def sorted(self):
        return (sorted((self.mark_1,self.mark_2,self.mark_3),reverse=True))

students=[Student_structure(111,"khush",77,88,95),
          Student_structure(112,"neha",50,65,87),
          Student_structure(113,"isha",76,99,98),
          Student_structure(114,"sanjana",50,45,40),
          Student_structure(115,"vidhi",98,99,99)]

for i in students:
    print("Total marks = ",i.total())
    print("The average marks = ",i.average())
    print("Descending of marks = ",i.sorted())
