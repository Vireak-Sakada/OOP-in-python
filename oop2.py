class student:
    
    class_year = 2024
    num_student = 0
    
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        student.num_student += 1
    #object
student1 = student("spongebob", 30)
student2 = student("Patrick", 35)
studento = student("sakada", 19)

print(student2.num_student)
#print(student1.age)
#print(student2.class_year)
print(f"my draduating student in{student.num_student} has {student.class_year} ")