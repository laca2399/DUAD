#Actions module, have all the operations related to the menu logic
#Student class with his attributes and init constructor
class Student:
    def __init__(self, name, section, spanish_grade, english_grade, science_grade, social_grade):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.science_grade = science_grade
        self.social_grade = social_grade
        self.average = self.calculate_average()

    def calculate_average(self):  #Student class method
        return (self.spanish_grade + self.english_grade + self.science_grade + self.social_grade) / 4
    
    def convert_to_dict (self):   #Student class method to convert to dictionary
        return {
            'Name': self.name,
            'Section': self.section,
            'Spanish': self.spanish_grade,
            'English': self.english_grade,
            'Science': self.science_grade,
            'Social': self.social_grade,
            'Average': self.average
        }

def obtain_student_quantity ():  #Function
    while True:
        try:
            student_quantity = input("Enter the quantity of students that you want to register: ")
            if student_quantity.isdigit() and int(student_quantity)>0: 
                #With isdigit we verified that the input is a whole positive number 
                return int(student_quantity)
            else:
                print("Error: The student quantity must be a positive whole number")
        except ValueError:
            print("Please enter a valid number: ")   

def obtain_grade(course):
    while True:
        try:
            grade = (input(f"Enter the grade for {course}, it must be between 0-100: "))
            grade = grade.replace(',', '.')  #In some countries we use "," instead of ".", so this is to replace that
            grade = float(grade)  #validate that grade is a float number
                
            if 0 <= grade <= 100:
                return grade
            else:
                print("Error: The grade must be a number between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")


def enter_student_info(students):

    quantity = obtain_student_quantity()

    for i in range (quantity):
        print(f"\\Student {i+1}:")
        #This will be print like: Student 1: , ... Student 2:

        name = input("Enter the student complete name: ")
        section = input("Enter the student section: ")

        spanish_grade = obtain_grade("spanish")
        english_grade = obtain_grade("english")
        science_grade = obtain_grade("science")
        social_grade = obtain_grade("social")

        student = Student(name, section, spanish_grade, english_grade, science_grade, social_grade)

        print(f"Created Student: {student.name}, Average: {student.average:.2f}")
        #print using object and attribute
        
        students.append(student)

        
def view_students_info(students):
    if not students:
        print ("No student information is available")
    else:
        print("\nInformation of all students:")
        for student in students:
            print(f"\nStudent: {student.name}")
            print(f"Section: {student.section}")
            print("Grades:")
            print(f"  Spanish: {student.spanish_grade}")
            print(f"  English: {student.english_grade}")
            print(f"  Science: {student.science_grade}")
            print(f"  Social Studies: {student.social_grade}")


def top3_students (students):
    if not students:
        print ("No student information is available")
        return
    
    student_averages = sorted(students, key=lambda student: student.average, reverse=True)
    #sorted: to organize
    #students, refers to the list of objects
    #key=lambda student: student.average:, sorting will be done based on the average attribute of each student
    #reverse = True, means from highest to lowest

    print("\nTop 3 Students with the Best Average Grade:")
    for i, student in enumerate(student_averages[:3]):  #top 3
        print(f"{i + 1}. {student.name} - Average: {student.average:.2f}") #print with max 2 decimals
        

def average_all_students(students):
    if not students:
        print ("No student information is available")
        return
    
    sum_average = 0
    student_count = len(students)

    for student in students:  #student = student name 
        sum_average += student.average  #student.average is the average attribute for each student

    total_average = sum_average / student_count

    print(f"\nThe Average Grade of all Students is: {total_average:.2f}")  #2f means with 2 decimal max

        