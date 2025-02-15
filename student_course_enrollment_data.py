import pandas as pd
import random

# Load the Students and Courses datasets
students_df = pd.read_csv("Processed_Students.csv")
courses_df = pd.read_csv("Courses.csv")

# Extract Student_IDs and Course_Codes
student_ids = students_df["Student_ID"].tolist()
course_codes = courses_df["Course_Code"].tolist()

# Function to generate random enrollment dates
def random_date():
    return f"202{random.randint(1, 3)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"

# Generate student-course enrollment data
enrollments = []
enrollment_id = 1

for student_id in student_ids:
    enrolled_courses = random.sample(course_codes, random.randint(1, min(5, len(course_codes))))  # Each student enrolls in 1-5 courses
    
    for course_code in enrolled_courses:
        enrollments.append([enrollment_id, student_id, course_code, random_date()])
        enrollment_id += 1

# Create DataFrame
df = pd.DataFrame(enrollments, columns=["Enrollment_ID", "Student_ID", "Course_Code", "Enrollment_Date"])

# Save to CSV
df.to_csv("Student_Course_Enrollment.csv", index=False)

print("Student_Course_Enrollment.csv file has been created!")
