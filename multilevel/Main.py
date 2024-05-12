from multilevel.Student import Student
from multilevel.StudentService import StudentService


class Main:
    def __init__(self):
        self.student_service = StudentService()

    def main(self):
        while True:
            print("1. Agregar estudiante")
            print("2. Listar estudiantes")
            print("3. Salir")
            choice = input("Elija una opción: ")

            if choice == "1":
                name = input("Nombre del estudiante: ")
                age = input("Edad del estudiante: ")
                student = Student(name, age)
                self.student_service.add_student(student)
            elif choice == "2":
                print("Lista de estudiantes:")
                for student in self.student_service.get_all_students():
                    print(f"Nombre: {student.name}, Edad: {student.age}")
            elif choice == "3":
                print("Saliendo del sistema.")
                break
            else:
                print("Opción no válida.")


if __name__ == "__main__":
    main = Main()
    main.main()