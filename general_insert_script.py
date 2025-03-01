import pandas as pd

# Load CSV file (update file name for different tables)
df = pd.read_csv("Processed_Grades.csv")

# Generate SQL INSERT statements
table_name = "Grades"
insert_statements = []

for _, row in df.iterrows():
    values = tuple(row)
    query = f"INSERT INTO {table_name} VALUES {values};"
    insert_statements.append(query)

# Save SQL queries to a file
with open(f"{table_name}_inserts.sql", "w") as file:
    file.write("\n".join(insert_statements))

print(f"SQL INSERT statements saved for {table_name}!")
