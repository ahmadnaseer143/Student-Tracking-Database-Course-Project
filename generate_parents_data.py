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
for parent_id, student_id in enumerate(student_ids, start=1):
    name = generate_name()
    email = generate_email(name)
    parents.append([parent_id, name, email, student_id])

# Create DataFrame
df = pd.DataFrame(parents, columns=["Parent_ID", "Name", "Contact_Info", "Student_ID"])

# Save to CSV
df.to_csv("Parents.csv", index=False)

print("Parents.csv file has been created!")
