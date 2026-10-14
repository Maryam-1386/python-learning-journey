class Student:
    def __init__(self,id , name , age , major):
        self.id= id
        self.name= name 
        self.age=age
        self.major = major
    
    def __str__(self):
        return f"ID:{self.id} | Name:{self.name} | Age:{self.age} | Major:{self.major}"
    
class StudentManager:
    def __init__(self):
        self.students=[]
    
    def add_student(self,student: Student):
        self.students.append(student)

    def show_students(self):
        for student in self.students:
            print(student)

    def find_student(self,student_id):
        for student in self.students:
            if student.id==student_id:
                return student
        return None

    def remove_student(self , student_id:int):
        student = self.find_student(student_id)
        if student:
                self.students.remove(student)
                return True
        return False
    
    def update_student(self,student_id: int , new_name:str , new_age:int , new_major:str):
        student = self.find_student(student_id)
        if student:
                student.name = new_name
                student.age = new_age
                student.major = new_major
                return True
        return False

    def  count_students(self):
        return len(self.students)

s1= Student(1,"maryam",20,"computer Engineer")
s2= Student(2,"yekta",23,"civacal Engineer")

manager = StudentManager()

manager.add_student(s1)
manager.add_student(s2)

manager.show_students()
print(manager.count_students())
print(manager.find_student(2))

manager.update_student(2, "Yekta", 24, "Architecture")

manager.show_students()

manager.remove_student(1)

manager.show_students()

print(manager.count_students())
