import pandas as pd
import random


students_df = pd.read_csv("Processed_Students.csv")
assignments_df = pd.read_csv("Assignments.csv")
enrollment_df = pd.read_csv("Student_Course_Enrollment.csv")

# Extract necessary columns from enrollment (Students & Courses)
student_courses = enrollment_df[["Student_ID", "Course_Code"]]

# From assignments, we only need Course_Code and Title, then rename Title to Assignment_Title
assignments = assignments_df[["Course_Code", "Title"]].rename(columns={"Title": "Assignment_Title"})

# Merge assignments with enrolled students based on Course_Code
grades_data = pd.merge(student_courses, assignments, on="Course_Code")
grades_data["Score"] = [round(random.uniform(0, 100), 2) for _ in range(len(grades_data))]
grades_data.insert(0, "Grade_ID", range(1, len(grades_data) + 1))

# Reorder columns to exactly match the desired order
grades_data = grades_data[["Grade_ID", "Student_ID", "Course_Code", "Assignment_Title", "Score"]]
grades_data.to_csv("Grades.csv", index=False)

print("Grades.csv file has been created successfully!")
