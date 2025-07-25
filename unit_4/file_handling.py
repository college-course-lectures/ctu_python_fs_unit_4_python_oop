# File object is created using open()
# Modes r, w, a, r+
import csv
import json

from torch.utils.hipify.hipify_python import openf

from unit_4.grading_system import Student


# r Read
#Opens the file for reading only
#File must exist
#Using the "with" keyword
def read_file(file):
    with open(file, 'r') as f:
        content = f.read()
        print(content)

def read_file_without_with(file):
    try:
        f = open(file, 'r')
        try:
            data = f.read()
        finally:
            f.close()
        print(data)
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


#Mode 'w' Write, opens the file for writing only
# It creates the file if it does not exist
#If file currently exist, it will overwrite the files content

def write_to_file():
    with open('python_file.txt', 'w') as f:
        f.write("Hello, New Python World!")

# Mode 'a' Append writes at the end of the current content
# create a new file if it does not exist
#Keep the existing content, adding new content to the end
def append_to_file():
    with open('another_file.txt', 'a') as f:
        f.write("Another line\n")

#Mode 'r+' Read and Write opens the file for both reading and writing
# Does not create the file if it does not exist
# seek() allows reading and writing from any point within file.  Moves the file cursor to a
#specified position
def read_write_file(file):
    with open(file, 'r+') as f:
        data = f.read()
        f.seek(0)
        f.write("Update")

#readline() returns only the first line
def read_line(file):
    with open(file, 'r') as f:
        line = f.readline()
        print(line)

#readlines() returns a list of all lines in a file
def read_all_lines(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        print(lines)

#Comma-Separated Values (CSV)
#format used to store tabular data in plain text
# Create a csv file with 3 students
#read the file using Python's open()
#Instanitiate (create objects) 3 Student objects from the file
#Iterate/Loop through Student object list and display each student using the __str__() method
def read_csv_create_student_object():
    students = []

    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = Student()
            student.set_student_info(row['name'], row['grade'], row['major'])
            students.append(student)

    for s in students:
        print(s)


 # json.dumps(): Convert Python object to JSON string
 # Invokes the to_dict() function in the Student class and returns a Student dictionary
 #Then converts Python dictionary to JSON
    students_json = json.dumps([s.to_dict() for s in students], indent=4)
    print("\nJSON Output:")
    print(students_json)

 #json.loads(): Convert JSON string to Python object.
    students_python_object = json.loads(students_json)
    print("\nPython Object Output:")
    print(students_python_object)


