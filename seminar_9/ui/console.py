from entities.student import Student
from entities.adress import Adress
class Console:
    def __init__(self, controller):
        self.controller = controller

    def menu(self):
        return """
            1 - add student
            2 - sort students
            0 - exit
            """

    def run(self):
        while True:
            print(self.menu())
            value = int(input())

            if value == 0:
                break

            if value == 1:
                id = int(input("enter id:"))
                name = input("enter name:")
                street = input("Street:")
                number = int(input("Streetnumber:"))
                student = Student(id, name, Adress(street, number))

                self.controller.addStudent(student)


            if value == 2:
                students = self.controller.sortStudents()

                for student in students:
                    print(student)
