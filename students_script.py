import pandas as pd
import random

# Load the Students CSV file
students_df = pd.read_csv("Processed_Students.csv")

# Rename and keep only necessary columns
students_df = students_df.rename(columns={'id': 'Student_ID', 'name': 'Name', 'age': 'Age'})
students_df = students_df[['Student_ID', 'Name', 'Age']]

# Generate random Grade_Level values
grade_levels = ['Freshman', 'Sophomore', 'Junior', 'Senior']
students_df['Grade_Level'] = [random.choice(grade_levels) for _ in range(len(students_df))]

# Load the Parents CSV file
parents_df = pd.read_csv("Parents.csv")

# Get the list of Parent_IDs
parent_ids = parents_df["Parent_ID"].tolist()

# Assign Parent_IDs randomly to students
students_df['Parent_ID'] = [random.choice(parent_ids) for _ in range(len(students_df))]

# Save the updated student data
students_df.to_csv("Processed_Students.csv", index=False)

print("Processed_Students.csv file has been updated with Parent_ID!")
