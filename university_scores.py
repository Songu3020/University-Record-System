def register_student():
    COURSES = (
        "Math", "Physics", "Computer Science", "Biology", "Chemistry",
        "Statistics", "English", "Economics", "History", "Philosophy",
        "Sociology", "Political Science", "Geography", "Psychology", "Art",
        "Music", "Engineering", "Law", "Medicine", "Business"
    )

    university_record = {}

    username = input("Enter username: ")

    while True:

        username = input("Enter username: ")
        if username in university_record:
            print("Username already exist")

        name = input("Enter name: ")
        if name = " ":
            print("name cannot be empty")
            return 
        age = int(input("Enter age: "))

        courses = input("Enter courses separated by comma: ")

        city = int 
        zip_code = int(input("enter your zip code: "))


    course = set()


    students = {
        "name": name,
        "age": age,
        "courses": courses,
        "address": {
                "city": city
                "zip_code": zip_code
        }
    }
    university_record[username] = students


    print("Student added successfully!")



def main():
        print("Welcome to University Scores!")
        print("1. Register student")
        print("2. Student")
        print("3. StudentId")

        choice = input("Enter an option")

        if choice == "1":
            register_student():

 
main()

