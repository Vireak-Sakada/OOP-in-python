#a class variable is a variable that is shared among all instances (objects) created from a specific class. 
class Student:
    class_year = 2024
    num_student = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_student +=1
#object create from the class
Student1 = Student("spongebob", 30)
Student2 = Student("Patrick", 35)
Student3 = Student("sakada", 19)
print(Student1.name)
print(Student1.age)
print(Student2.name)
print(Student.class_year)
print(Student.num_student)
print(f"My graduating class of {Student.class_year}has{Student.num_student}")
print(Student1.name)
print(Student2.name)
print(Student3.name)