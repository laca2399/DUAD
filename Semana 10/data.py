#Module data, have the other logic options like import and export 

import csv
import os

def export_to_csv(students):
    if not students:
        print ("No student information is available")
        return
    

    with open ("students.csv", "w", newline = "", encoding = "utf-8") as csvfile:
        fieldnames = ['Name', 'Section', 'Spanish', 'English', 'Science', 'Social', 'Average']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #students.csv will be the name of the file when is created
        #"w", is what we use for writing the file
        #newline is basically to prevent extra blank lines
        #fieldnames is the list of the column names (headers)
        #csv.DictWriter, allows to write the dictionary into the csv file

        writer.writeheader()  #write the field names as the first row of the CSV file, separated by commas.
        for name, details in students.items():
            student_data = {
                'Name': name,
                'Section': details['Section'],
                'Spanish': details['Grades']['Spanish'],
                'English': details['Grades']['English'],
                'Science': details['Grades']['Science'],
                'Social': details['Grades']['Social Studies'],
                'Average': details['Average']
            }
            writer.writerow(student_data)

    print("Student data exported to 'students.csv' successfully.")

def import_from_csv(students):
    if not os.path.exists('students.csv'):  #is to validate if the file we want to import, exists¿s in the OS
        print("No previous student data found. The 'students.csv' file does not exist.")
        return
    
    with open('students.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        #"r", is for reader

        for row in reader:
            
            name = row['Name']
            section = row['Section']
            spanish_grade = float(row['Spanish'])
            english_grade = float(row['English'])
            science_grade = float(row['Science'])
            social_grade = float(row['Social'])
            average = float(row['Average'])

            students[name] = {
                "Section": section,
                "Grades": {
                    "Spanish": spanish_grade,
                    "English": english_grade,
                    "Science": science_grade,
                    "Social Studies": social_grade
                },
                "Average": average
            }

    print("Student data imported from 'students.csv' successfully.")
