import mysql.connector

# Database connection details
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "password"
DB_NAME = "studentperformancedb"

try:
    # Step 1: Connect to the MySQL database
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    if connection.is_connected():
        print("Connected to the database successfully!")

    # Step 2: Create a cursor object to execute queries
    cursor = connection.cursor()

    # Step 3: SQL query to fetch student grades
    query = """
    SELECT Students.Student_ID, Students.Name, Grades.Assignment_Title, Grades.Score
    FROM Students
    INNER JOIN Grades ON Students.Student_ID = Grades.Student_ID
    ORDER BY Students.Student_ID;
    """

    cursor.execute(query)

    # Step 4: Fetch all results
    results = cursor.fetchall()

    # Step 5: Display results on the screen
    print("\nStudent Grades Report:")
    print("=" * 50)
    for row in results:
        student_id, student_name, assignment_title, score = row
        print(f"ID: {student_id}, Name: {student_name}, Assignment: {assignment_title}, Score: {score}")

    # Step 6: Save the results to a text file
    with open("student_grades_report.txt", "w") as file:
        file.write("Student Grades Report\n")
        file.write("=" * 50 + "\n")
        for row in results:
            file.write(f"ID: {row[0]}, Name: {row[1]}, Assignment: {row[2]}, Score: {row[3]}\n")

    print("\nReport saved as 'student_grades_report.txt'.")

except mysql.connector.Error as error:
    print("Error connecting to MySQL:", error)

finally:
    # Step 7: Close the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Database connection closed.")
