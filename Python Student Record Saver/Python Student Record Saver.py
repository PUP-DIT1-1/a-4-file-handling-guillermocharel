while True: 
    print("\nWelcome to the Student Record System!")
    print("\nStudent Record Menu") 
    print("1 - Add Student Record") 
    print("2 - View Saved Records") 
    print("3 - Exit Program") 

    choice = input("Enter your choice (1-3): ") 
    if choice == "1": 
        name = input("Enter student name: ") 
        grade = input("Enter student grade: ") 
 
        with open("studentdata.txt", "a") as file: 
            file.write(name + ", " + grade + "\n") 
            print("Student record added successfully.") 
 
    elif choice == "2": 
        try: 
            with open("studentdata.txt", "r") as file:
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
        print("\nExiting program... Thank you for using the Student Record System!") 
        break 
 
    else: 
        print("Invalid choice. Please try again.") 
