from ui.console import Console
from logic.controller import Controller
#from repository.studentRepository import StudentRepo
from repository.studentRepository import FileStudentRepository

def main():

    console = Console(Controller(FileStudentRepository('students.dat')))

    console.run()

main()

