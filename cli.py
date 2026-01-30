students = {}

def add_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    course = input("Enter Course: ")
    students[sid] = {"name": name, "marks": marks, "course": course}
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No records found.\n")
    else:
        for sid, details in students.items():
            print(f"ID: {sid}, Name: {details['name']}, Marks: {details['marks']}, Course: {details['course']}")
        print()

def search_student():
    sid = int(input("Enter Student ID to search: "))
    if sid in students:
        s = students[sid]
        print(f"Name: {s['name']}, Marks: {s['marks']}, Course: {s['course']}\n")
    else:
        print("Student not found!\n")

def update_student():
    sid = int(input("Enter Student ID to update: "))
    if sid in students:
        students[sid]["name"] = input("Enter new name: ")
        students[sid]["marks"] = int(input("Enter new marks: "))
        students[sid]["course"] = input("Enter new course: ")
        print("Student updated successfully!\n")
    else:
        print("Student not found!\n")

def delete_student():
    sid = int(input("Enter Student ID to delete: "))
    if sid in students:
        del students[sid]
        print("Student deleted successfully!\n")
    else:
        print("Student not found!\n")

while True:
    print("=== Student Record Manager ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")
