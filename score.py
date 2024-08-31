"""
Quang Nguyen
score.py
An app that will take student's first name, last name, and GPA to determine whether they make it for Dean's List or Honor Roll. 
-first_name will be used to take input of the first name
-last_name will be used to take input of the last name, and if last name is input as 'ZZZ', the program will be terminate
-gpa is used to take input of GPA. With input of >= 3.25, the student will make the Honor Roll, and input of >= 3.5 will make to the Dean's List.
"""


while True: 
    last_name = input("Enter your last name (if you put 'ZZZ' the program will exit): ")
    if last_name == 'ZZZ': 
        break

    first_name = input("Enter first name: ")
    gpa = float(input("Enter your GPA: "))

    if gpa >= 3.5: 
        print("You have made Dean's List.")
    elif gpa >= 3.25: 
        print("You have made the Honor Roll.")

    
