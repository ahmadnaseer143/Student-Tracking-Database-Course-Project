import pandas as pd
import random

# Load student course enrollment data
enrollment_df = pd.read_csv("Student_Course_Enrollment.csv")

# Extract necessary columns
attendance_data = enrollment_df[["Student_ID", "Course_Code"]].copy()

# Generate random attendance percentages (0 to 100)
attendance_data["Attendance_Percentage"] = [round(random.uniform(50, 100), 2) for _ in range(len(attendance_data))]

# Assign unique Attendance_ID
attendance_data.insert(0, "Attendance_ID", range(1, len(attendance_data) + 1))

# Save to CSV
attendance_data.to_csv("Attendance.csv", index=False)

print("Attendance.csv file has been created successfully!")
