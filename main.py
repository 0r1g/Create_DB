import sqlite3


def connect_db():
    return sqlite3.connect('university.db')


def add_student(name, age, major):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO students (name, age, major) VALUES (?, ?, ?)
    ''', (name, age, major))
    conn.commit()
    conn.close()


def add_course(course_name, instructor):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO courses (course_name, instructor) VALUES (?, ?)
    ''', (course_name, instructor))
    conn.commit()
    conn.close()


def enroll_student(student_id, course_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR IGNORE INTO student_courses (student_id, course_id) VALUES (?, ?)
    ''', (student_id, course_id))
    conn.commit()
    conn.close()


def get_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students


def get_courses():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses')
    courses = cursor.fetchall()
    conn.close()
    return courses


def get_students_by_course(course_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT s.id, s.name, s.age, s.major
    FROM students s
    INNER JOIN student_courses sc ON s.id = sc.student_id
    WHERE sc.course_id = ?
    ''', (course_id,))
    students = cursor.fetchall()
    conn.close()
    return students


def main():
    while True:
        print("\nUniversity Database System")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. View Students")
        print("5. View Courses")
        print("6. View Students by Course")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            major = input("Enter student major: ")
            add_student(name, age, major)
            print("Student added successfully.")

        elif choice == '2':
            course_name = input("Enter course name: ")
            instructor = input("Enter instructor name: ")
            add_course(course_name, instructor)
            print("Course added successfully.")

        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            enroll_student(student_id, course_id)
            print("Student enrolled in course successfully.")

        elif choice == '4':
            students = get_students()
            for student in students:
                print(student)

        elif choice == '5':
            courses = get_courses()
            for course in courses:
                print(course)

        elif choice == '6':
            course_id = int(input("Enter course ID: "))
            students = get_students_by_course(course_id)
            for student in students:
                print(student)

        elif choice == '7':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
