class Student:
    # __init__ initializes the attributes, it's usually the first method in a class - initializer of object
    def __init__(self):
        self.__name = " "
        self.__grade = 0.0
        self.__major = " "

    def enter_student_info(self):
        self.__name = input("Enter student name: ")
        self.__grade = (float(input("Enter student grade: ")))
        self.__major = input("Enter student's major: ")

    def get_student_data(self):
        print("Student Name: ", self.__name, "Grade: " , self.__grade, "Major: ", self.__major)

    #View the state of the current object. The state is the value of the objects attributes
    def __str__(self):
        return f"{self.__name} is majoring in {self.__major} with a current grade of {self.__grade: .2f}."


class JuniorStudent(Student):
    def __init__(self):
        super().__init__()
        self.__internship_required = True

    def __str__(self):
        base_info = super().__str__() # Allows child class to reuse parent methods
        return f"{base_info} This student is a Junior.  Internship required: {self.__internship_required}."



class SeniorStudent(Student):
    def __init__(self):
        super().__init__()
        self.__capstone_project_title = " "

    def enter_student_info(self):
        super().enter_student_info()
        self.__capstone_project_title = input("Enter capstone project title: ")

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info} This student is a Senior working on a project titled '{self.__capstone_project_title}'."



