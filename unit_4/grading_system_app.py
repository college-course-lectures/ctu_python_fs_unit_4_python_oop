from grading_system import Student, JuniorStudent, SeniorStudent


def main():
    # student = Student() #creates a student object / instance
    # student.enter_student_info()
    # student.get_student_data()
    # print(student)

    # junior = JuniorStudent()
    # junior.enter_student_info()
    # print(junior)

    senior = SeniorStudent()
    senior.enter_student_info()
    print(senior)

#Call the main function
if __name__ == '__main__':
    main()