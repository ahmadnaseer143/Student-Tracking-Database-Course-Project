import pandas as pd
import random

# Load necessary data files
students_df = pd.read_csv("Processed_Students.csv")
assignments_df = pd.read_csv("Assignments.csv")
enrollment_df = pd.read_csv("Student_Course_Enrollment.csv")

# Extract only relevant columns from enrollment (Students & Courses)
student_courses = enrollment_df[["Student_ID", "Course_Code"]]

# Extract only relevant columns from assignments and rename "Title" to "Assignment_Title"
assignments = assignments_df[["Assignment_ID", "Course_Code", "Title"]].rename(columns={"Title": "Assignment_Title"})

# Merge assignments with enrolled students based on Course_Code
grades_data = pd.merge(student_courses, assignments, on="Course_Code")

# Generate random scores between 0 and 100
grades_data["Score"] = [round(random.uniform(0, 100), 2) for _ in range(len(grades_data))]

# Assign unique Grade_ID
grades_data.insert(0, "Grade_ID", range(1, len(grades_data) + 1))

# Keep only the required columns in the correct order
grades_data = grades_data[["Grade_ID", "Assignment_Title", "Score", "Assignment_ID", "Student_ID"]]

# Save the final CSV file
grades_data.to_csv("Grades.csv", index=False)

print("Grades.csv file has been created successfully!")
