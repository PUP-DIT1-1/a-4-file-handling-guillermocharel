while True:
    print("\nWelcome to the Student Record System!")
    print("\nStudent Record Menu")
    print("1. Add Student Record")
    print("2. View Student Records")
    print("3. Update Student Record")
    print("4. Delete Student Record")
    print("5. Exit Program")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        with open("students.txt", "a") as file:
            file.write(f"{name}, {age}, {grade}\n")
        print("Student record added successfully.")
    elif choice == "2":
        try:
            with open("students.txt", "r") as file:
                records = file.readlines()
                if records:
                    print("\nStudent Records:")
                    for record in records:
                        print(record.strip())
                else:
                    print("No student records found.")
        except FileNotFoundError:
            print("No student records found.")
    elif choice == "3":
        name = input("Enter the name of the student to update: ")
        try:
            with open("students.txt", "r") as file:
                records = file.readlines()
            updated_records = []
            found = False
            for record in records:
                if record.startswith(name + ","):
                    age = input("Enter new age: ")
                    grade = input("Enter new grade: ")
                    updated_records.append(f"{name}, {age}, {grade}\n")
                    found = True
                else:
                    updated_records.append(record)
            if found:
                with open("students.txt", "w") as file:
                    file.writelines(updated_records)
                print("Student record updated successfully.")
            else:
                print("Student record not found.")
        except FileNotFoundError:
            print("No student records found.")
    elif choice == "4":
        name = input("Enter the name of the student to delete: ")
        try:
            with open("students.txt", "r") as file:
                records = file.readlines()
            updated_records = [
                record for record in records if not record.startswith(name + ",")
            ]
            if len(updated_records) < len(records):
                with open("students.txt", "w") as file:
                    file.writelines(updated_records)
                print("Student record deleted successfully.")
            else:
                print("Student record not found.")
        except FileNotFoundError:
            print("No student records found.")
    elif choice == "5":
        print("\nExiting the program... Thank you for using the Student Record System!")
        break
    else:
        print("Invalid choice. Please try again.")
