from menudup import menu   
from actionsdup import enter_student_info, view_students_info, top3_students, average_all_students
from datadup import export_to_csv, import_from_csv

import os   #It allows more easily way to handle and find files in the OS

def main():    
    #Point of entry of the program
    students = []  

    while True:
        menu()

        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:
            enter_student_info(students)
        elif option == 2:
            view_students_info(students)
        elif option == 3: 
            top3_students (students)
        elif option == 4:
            average_all_students(students)
        elif option == 5:
            export_to_csv(students)
        elif option == 6:
            import_from_csv(students)
        elif option == 0:
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please select a valid option.")   

if __name__ == "__main__":
    main()

