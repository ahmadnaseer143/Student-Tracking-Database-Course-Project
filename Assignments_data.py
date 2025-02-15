import pandas as pd
import random

# Load the Courses dataset
courses_df = pd.read_csv("Courses.csv")

# Extract Course_Codes
course_codes = courses_df["Course_Code"].tolist()

# Function to generate random due dates
def random_date():
    return f"202{random.randint(1, 3)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"

# Assignment Titles Pool
assignment_titles = [
    "Homework 1", "Project 1", "Quiz 1", "Midterm Exam", "Final Exam",
    "Research Paper", "Presentation", "Lab Report", "Discussion Board", "Case Study"
]

# Generate assignments data
assignments = []
assignment_id = 1

for course_code in course_codes:
    num_assignments = random.randint(2, 6)  # Each course has 2-6 assignments
    selected_titles = random.sample(assignment_titles, num_assignments)  # Random unique titles for each course
    
    for title in selected_titles:
        max_score = random.choice([50, 100])  # Max score is either 50 or 100
        assignments.append([assignment_id, course_code, title, random_date(), max_score])
        assignment_id += 1

# Create DataFrame
df = pd.DataFrame(assignments, columns=["Assignment_ID", "Course_Code", "Title", "Due_Date", "Max_Score"])

# Save to CSV
df.to_csv("Assignments.csv", index=False)

print("Assignments.csv file has been created!")
