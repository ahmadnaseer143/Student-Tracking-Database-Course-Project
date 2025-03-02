import pandas as pd
import random

# Load student course enrollment data
enrollment_df = pd.read_csv("Student_Course_Enrollment.csv")

# Load course data
courses_df = pd.read_csv("Courses.csv")

# Extract necessary columns in the correct order
attendance_data = enrollment_df[["Student_ID"]].copy()

# Randomly assign Course_Code from the Courses.csv file
attendance_data["Course_Code"] = [random.choice(courses_df["Course_Code"].tolist()) for _ in range(len(attendance_data))]

# Generate random attendance percentages (50 to 100)
attendance_data.insert(1, "Attendance_Percentage", [round(random.uniform(50, 100), 2) for _ in range(len(attendance_data))])

# Assign unique Attendance_ID in the first column
attendance_data.insert(0, "Attendance_ID", range(1, len(attendance_data) + 1))

# Save to CSV in the required column order
attendance_data.to_csv("Attendance.csv", index=False)

print("Attendance.csv file has been created successfully!")
