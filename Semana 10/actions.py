#Actions module, have all the operations related to the menu logic

def obtain_student_quantity ():
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
        print(f"\Student {i+1}:")
        #This will be print like: Student 1: , ... Student 2:

        name = input("Enter the student complete name: ")
        section = input("Enter the student section: ")

        spanish_grade = obtain_grade("spanish")
        english_grade = obtain_grade("english")
        science_grade = obtain_grade("science")
        social_grade = obtain_grade("social")

        average_grade = (spanish_grade + english_grade + science_grade + social_grade) / 4
        #Formula to calculate average for student, so we reduce steps

        #Storage info as:
        students[name] = {
            "Section": section,
            "Grades": {
                "Spanish": spanish_grade,
                "English": english_grade,
                "Science": science_grade,
                "Social Studies": social_grade
            },
            "Average": average_grade
        }

def view_students_info(students):
    if not students:
        print ("No student information is available")
    else:
        print("\nInformation of all students:")
        for name, details in students.items():  #method items(), return iterable of key-value pairs
            #name refers to the key, and details refers to the values
            print(f"\nStudent: {name}")
            print(f"Section: {details['Section']}")
            print("Grades:")
            for subject, grade in details['Grades'].items():
                print(f"  {subject}: {grade}")

def top3_students (students):
    if not students:
        print ("No student information is available")
        return
    
    student_averages = sorted(students.items(), key=lambda x: x[1]['Average'], reverse=True)
    #sorted is for organize
    #x represents each item from the iterable (name, details)
    #x[1] refers to the second element in the tuple, which is the details dictionary for each student.
    #['Average'] to access the average of each student

    print("\nTop 3 Students with the Best Average Grade:")
    for i, (name, details) in enumerate(student_averages[:3]):  #Maximum 3 because is the top3
        print(f"{i + 1}. {name} - Average: {details['Average']:.2f}")  #2f means with 2 decimal max
        

def average_all_students(students):
    if not students:
        print ("No student information is available")
        return
    
    sum_average = 0
    student_count = len(students)

    for student, details in students.items():  #student = student name 
        sum_average += details['Average']

    total_average = sum_average / student_count

    print(f"\nThe Average Grade of all Students is: {total_average:.2f}")  #2f means with 2 decimal max

        