import sqlite3

DB_STUDENTS="students.db"


# Data connection
def connect_db():

    return sqlite3.connect(DB_STUDENTS)



# new table
def create_table():

    try:
        conn=connect_db()

        cursor=conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY,name TEXT NOT NULL,grade TEXT NOT NULL,email TEXT NOT NULL)""")

        conn.commit()

        conn.close()

    except sqlite3.Error as e:

        print( "database error:", e )


# Add new student 
def add_student():

    try:

        name=input( "Enter student name: " ).strip()

        grade=input( "Enter student grade: " ).strip()

        email=input( "Enter student email: " ).strip()

        if "@" not in email:
            print( "Invalid email format." )
            return

        conn=connect_db()

        cursor=conn.cursor()

        cursor.execute(
            "INSERT INTO students (name,grade,email) VALUES (?, ?, ?)",
            (name,grade,email)
        )

        conn.commit()

        conn.close()

        print( "Student added successfully." )

    except sqlite3.Error as e:

        print( "error adding student data:", e )


# View students data
def view_students():

    try:

        conn=connect_db()

        cursor=conn.cursor()

        cursor.execute("SELECT * FROM students")

        records=cursor.fetchall()

        conn.close()


        if not records:

            print( "No student records found." )

        else:

            for student in records:

                print(student)

    except sqlite3.Error as e:

        print( "error reading student data:", e )


# Update data
def update_student():

    try:

        student_id=int(input( "Enter student ID to update: " ))

        name=input( "New name: " ).strip()

        grade=input( "New grade: " ).strip()

        email=input( "New email: " ).strip()


        if "@" not in email:

            print( "Invalid email format." )

            return

        conn=connect_db()

        cursor=conn.cursor()

        cursor.execute("""
            
            UPDATE students
            SET name=?,grade=?,email=?
            WHERE id=?
        """, (name,grade,email,student_id))

        if cursor.rowcount == 0:

            print( "student ID not found." )

        else:

            print( "student data updated successfully." )

        conn.commit()

        conn.close()


    except ValueError:

        print( "ID must be an integer." )

    except sqlite3.Error as e:

        print( "Error updating student:", e )


#delete student data
def delete_student():

    try:

        student_id=int(input( "Enter student ID to delete: " ))

        confirm=input( "Are you sure? (y/n): " ).lower()

        if confirm != "y":

            print( "Delete cancelled." )

            return

        conn=connect_db()
        
        cursor=conn.cursor()

        cursor.execute("DELETE FROM students WHERE id = ?",(student_id,))

        if cursor.rowcount==0:

            print( "student ID not found." )

        else:

            print( "student data deleted successfully." )

        conn.commit()

        conn.close()

    except ValueError:

        print( "ID must be an integer." )

    except sqlite3.Error as e:

        print( "error deleting student data:", e )


# Menu
def menu():

    print( "\nStudent Records Management" )

    print( "1. Add Student in the database" )

    print( "2. View Students database" )

    print( "3. Update Student database" )

    print( "4. Delete Student from database" )

    print( "5. Exit program" )



# Main 
def main():

    create_table()

    while True:

        menu()

        choice=input( "Choose an option between 1 to 5: " )

        if choice==  "1":

            add_student()

        elif choice== "2":

            view_students()

        elif choice== "3":

            update_student()

        elif choice== "4":

            delete_student()

        elif choice== "5":

            print("Goodbye, exit program.")

            break

        else:

            print("Invalid pick.")


if __name__ == "__main__":
    main()