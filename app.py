from services.student_service import create_student, get_students
from services.club_service import create_club
from services.membership_service import add_student_to_club


def main():
    while True:
        print("\n=== SCHOOL CLUB SYSTEM ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add Club")
        print("4. Assign Student to Club")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            create_student(name, email)

        elif choice == "2":
            get_students()

        elif choice == "3":
            name = input("Club Name: ")
            desc = input("Description: ")
            create_club(name, desc)

        elif choice == "4":
            student_id = input("Student ID: ")
            club_id = input("Club ID: ")
            add_student_to_club(student_id, club_id)

        elif choice == "5":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
