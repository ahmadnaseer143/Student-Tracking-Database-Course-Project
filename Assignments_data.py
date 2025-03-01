import pandas as pd
import random

# Load the Courses dataset
courses_df = pd.read_csv("Courses.csv")

# Extract Course_Code
course_codes = courses_df["Course_Code"].tolist()

# Function to generate random due dates
def random_date():
    year = random.randint(2021, 2023)  # Ensure proper year format
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Avoid invalid dates like Feb 30
    return f"{year}-{month:02d}-{day:02d}"

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
        due_date = random_date()  # Ensure correct date format
        assignments.append([assignment_id, title, due_date, max_score, course_code])
        assignment_id += 1

# Create DataFrame
df = pd.DataFrame(assignments, columns=["Assignment_ID", "Title", "Due_Date", "Max_Score", "Course_Code"])

# Save to CSV
df.to_csv("Assignments.csv", index=False)

print("Assignments.csv file has been created!")
