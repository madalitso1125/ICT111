"""
Application: Student Grading System
Course: ICT111 Principles of Programming (Python & Git)
Institution: Mulungushi University
"""

def grading_system():
    students = []

    while True:
        print("\n========================================")
        print("       MULUNGUSHI UNIVERSITY            ")
        print("     STUDENT GRADING SYSTEM             ")
        print("========================================")
        print("1. Add student")
        print("2. Display all")
        print("3. Class summary")
        print("4. Exit")
        
        option = input("Choose 1-4: ").strip()

        if option == "1":
            # 1. Validate Student Number
            while True:
                student_number = input("Enter student number: ").strip()
                if student_number:
                    break
                print("[Error] Student number cannot be blank. Please try again.")

            # 2. Validate Name
            while True:
                name = input("Enter student name: ").strip()
                if name:
                    break
                print("[Error] Name cannot be blank. Please try again.")

            # 3. Validate Mark (0-100, non-crash numeric check)
            while True:
                mark_input = input("Enter mark (0-100): ").strip()
                try:
                    mark = float(mark_input)
                    if 0 <= mark <= 100:
                        if mark.is_integer():
                            mark = int(mark)
                        break
                    else:
                        print("[Error] Mark must be between 0 and 100.")
                except ValueError:
                    print("[Error] Invalid input. Please enter a numeric value.")

            # 4. Determine Grade and Decision using if/elif/else
            if mark >= 80:
                grade = 'A'
                decision = 'Excellent'
            elif mark >= 70:
                grade = 'B'
                decision = 'Very good'
            elif mark >= 60:
                grade = 'C'
                decision = 'Good'
            elif mark >= 50:
                grade = 'D'
                decision = 'Pass'
            else:
                grade = 'F'
                decision = 'Fail'

            # 5. Store record as a dictionary inside the students list
            student_record = {
                "student_number": student_number,
                "name": name,
                "mark": mark,
                "grade": grade,
                "decision": decision
            }
            students.append(student_record)
            print(f"\n[Success] Record added for {name} ({student_number}) -> Grade: {grade} ({decision})")

        elif option == "2":
            print("\n------------------------------------------------------------------")
            print(f"{'Student No':<15} | {'Name':<20} | {'Mark':<6} | {'Grade':<6} | {'Decision':<10}")
            print("------------------------------------------------------------------")
            if not students:
                print("No student records exist yet.")
            else:
                for s in students:
                    print(f"{s['student_number']:<15} | {s['name']:<20} | {s['mark']:<6} | {s['grade']:<6} | {s['decision']:<10}")
            print("------------------------------------------------------------------")

        elif option == "3":
            print("\n================ CLASS STATISTICS ================")
            if not students:
                print("No student records exist yet. Cannot compute statistics.")
            else:
                total_students = len(students)
                total_marks = 0
                highest_mark = students[0]['mark']
                lowest_mark = students[0]['mark']
                passes = 0
                fails = 0

                for s in students:
                    m = s['mark']
                    total_marks += m
                    if m > highest_mark:
                        highest_mark = m
                    if m < lowest_mark:
                        lowest_mark = m
                    
                    if m >= 50:
                        passes += 1
                    else:
                        fails += 1

                class_average = total_marks / total_students

                print(f"Total Students : {total_students}")
                print(f"Class Average  : {class_average:.2f}")
                print(f"Highest Mark   : {highest_mark}")
                print(f"Lowest Mark    : {lowest_mark}")
                print(f"Passes (>= 50) : {passes}")
                print(f"Fails (< 50)   : {fails}")
            print("==================================================")

        elif option == "4":
            print("\nExiting Student Grading System. Goodbye!")
            break

        else:
            print("\n[Warning] Invalid option. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    grading_system()