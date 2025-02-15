import pandas as pd
import random

# Function to generate random names
first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Robert", "Laura", "James", "Olivia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

def generate_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate random email addresses
domains = ["school.edu", "education.org", "teacher.com"]
def generate_email(name):
    return name.lower().replace(" ", ".") + f"@{random.choice(domains)}"

# Number of teachers to generate
num_teachers = 100  # You can increase this as needed

# Generate teacher data
teachers = []
for emp_id in range(1, num_teachers + 1):
    name = generate_name()
    email = generate_email(name)
    teachers.append([emp_id, name, email])

# Create DataFrame
df = pd.DataFrame(teachers, columns=["Employee_ID", "Name", "Contact_Info"])

# Save to CSV
df.to_csv("Teachers.csv", index=False)

print("Teachers.csv file has been created!")
