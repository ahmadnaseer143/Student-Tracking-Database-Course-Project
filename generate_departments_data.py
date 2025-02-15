import pandas as pd
import random

# List of sample department names
department_names = [
    "Computer Science", "Mathematics", "Physics", "Biology", "Chemistry",
    "History", "English", "Economics", "Psychology", "Engineering"
]

# Function to generate random names for department heads
first_names = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Helen"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Davis", "Martinez"]

def generate_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Number of departments to generate
num_departments = len(department_names)

# Generate department data
departments = []
for dept_id in range(1, num_departments + 1):
    dept_name = department_names[dept_id - 1]  # Ensure unique department names
    dept_head = generate_name()
    departments.append([dept_id, dept_name, dept_head])

# Create DataFrame
df = pd.DataFrame(departments, columns=["Department_ID", "Name", "Head"])

# Save to CSV
df.to_csv("Departments.csv", index=False)

print("Departments.csv file has been created!")
