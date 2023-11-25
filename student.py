class Student:
    school_name='ABC School'
    def __init__ (self,name,age):
        self.name=name
        self.age=age
s1=Student("HARRY",20)
print('Student:',s1.name,s1.age)
print('school_name:',Student.school_name)
s1.name="JEESSA"
s1.age=19
print('school_name:',s1.name,s1.age)
Student.school_name='XYZ SCHOOL'
print('school_name:',Student.school_name)



