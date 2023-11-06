from student import Student

student1 = Student("Patil", 23)
print(student1.getname())
print(student1.getage())


student2 = Student("Paliwal", 24)
student2.incrementAge(2)
print(student2.getname() + " has age is " , student2.getage())
