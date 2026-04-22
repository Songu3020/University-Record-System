class Department:
    COURSES = (
        "Math", "Physics", "Computer Science", "Biology", "Chemistry",
        "Statistics", "English", "Economics", "History", "Philosophy",
        "Sociology", "Political Science", "Geography", "Psychology", "Art",
        "Music", "Engineering", "Law", "Medicine", "Business"
    )

    students = {}

    name = input("Enter name: ")
    age = int(input("Enter age: "))

    courses = input("Enter courses separated by comma: ")

    address = input("Enter address: ")

    student = {
        "name": name,
        "age": age,
        "courses": courses,
        "address": address
    }



    print("Student added successfully!")



def main():
        print("Welcome to University Scores!")
        print("1. Department")
        print("2. Student")
        print("3. StudentId")

        age = int(input("Enter department : "))
        name = input("Enter Student Name : ")
        courses = input("Enter s: ")
main()

