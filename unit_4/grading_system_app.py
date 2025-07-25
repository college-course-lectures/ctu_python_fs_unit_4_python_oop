from fontTools.afmLib import readlines

from grading_system import Student, JuniorStudent, SeniorStudent
from unit_4.file_handling import read_file, read_file_without_with, write_to_file, append_to_file, read_write_file, \
    read_line, read_all_lines, read_csv_create_student_object


def main():
    # student = Student() #creates a student object / instance
    # student.enter_student_info()
    # student.get_student_data()
    # print(student)

    # junior = JuniorStudent()
    # junior.enter_student_info()
    # print(junior)

     # senior = SeniorStudent()
     # senior.enter_student_info()
     # print(senior)

     #File Handling
     #read_file("file.txt")
     #read_file_without_with("file1.txt")
     #write_to_file()
     # append_to_file()
     #read_write_file("file.txt")
     #read_line("courses.txt")
     #read_all_lines("courses.txt")
     read_csv_create_student_object()





#Call the main function
if __name__ == '__main__':
    main()