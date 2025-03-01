import pandas as pd
import random

# Load the existing students data
students_df = pd.read_csv("Processed_Students.csv")

# Extract Student_IDs
student_ids = students_df["Student_ID"].tolist()

# Function to generate random parent names
first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Robert", "Laura", "James", "Olivia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

def generate_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate random email addresses
domains = ["gmail.com", "yahoo.com", "outlook.com"]
def generate_email(name):
    return name.lower().replace(" ", ".") + f"@{random.choice(domains)}"

# Generate parents data
parents = []
student_parent_mapping = {}

for parent_id, student_id in enumerate(student_ids, start=1):
    name = generate_name()
    email = generate_email(name)
    parents.append([parent_id, name, email])
    student_parent_mapping[student_id] = parent_id  # Link student to parent

# Create Parents DataFrame
parents_df = pd.DataFrame(parents, columns=["Parent_ID", "Name", "Email"])

# Save to CSV
parents_df.to_csv("Parents.csv", index=False)

# Update Students table with Parent_ID
students_df["Parent_ID"] = students_df["Student_ID"].map(student_parent_mapping)

# Save updated Students data
students_df.to_csv("Processed_Students.csv", index=False)

print("Parents.csv and updated Processed_Students.csv files have been created!")
