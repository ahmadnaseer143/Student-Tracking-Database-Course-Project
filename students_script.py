import pandas as pd
import random

# Load the CSV file
df = pd.read_csv("Students.csv")

# Rename and keep only necessary columns
df = df.rename(columns={'id': 'Student_ID', 'name': 'Name', 'age': 'Age'})
df = df[['Student_ID', 'Name', 'Age']]

# Generate random Grade_Level values
grade_levels = ['Freshman', 'Sophomore', 'Junior', 'Senior']
df['Grade_Level'] = [random.choice(grade_levels) for _ in range(len(df))]

# Generate random Parent_Contact_Info (fake emails)
domains = ["gmail.com", "yahoo.com", "outlook.com"]
df['Parent_Contact_Info'] = [f"parent{sid}@{random.choice(domains)}" for sid in df['Student_ID']]

# Save the processed data
df.to_csv("Processed_Students.csv", index=False)

print("Processed_Students.csv file has been created!")
