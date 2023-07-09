import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('E:/556 a1/dataset4.csv' )

# a. Find the total number of male and female employees
gender_counts = df['Gender'].value_counts()
print("Total number of male employees:", gender_counts['male'])
print("Total number of female employees:", gender_counts['female'])

# b. Find the total number of single, married, and divorced employees
marital_status_counts = df['Marital Status'].value_counts()
print("Total number of single employees:", marital_status_counts['single'])
print("Total number of married employees:", marital_status_counts['married'])
print("Total number of divorced employees:", marital_status_counts['divorced'])

# c. Find the employee IDs of managers
manager_ids = df[df['Designation'] == 'Manager']['Employee ID']
print("Employee IDs of managers:", manager_ids.tolist())

# d. Find the employee IDs of supervisors
supervisor_ids = df[df['Designation'] == 'Supervisor']['Employee ID']
print("Employee IDs of supervisors:", supervisor_ids.tolist())

# e. Clean the dataset by replacing empty records with 0 or deleting incomplete data rows
df.fillna(0, inplace=True)  # Replace empty records with 0
df.dropna(inplace=True)  # Delete incomplete data rows

# f. Find the names of employees who are working as managers and from Pune
managers_from_pune = df[(df['Designation'] == 'Manager') & (df['City'] == 'Pune')]['Name']
print("Names of employees working as managers from Pune:", managers_from_pune.tolist())

# g. Find the employees whose salary is greater than 1,00,000/-
high_salary_employees = df[df['Salary'] > 100000]['Name']
print("Names of employees with a salary greater than 1,00,000/-:", high_salary_employees.tolist())
