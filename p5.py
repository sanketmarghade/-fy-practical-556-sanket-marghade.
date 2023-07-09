
import pandas as pd

df = pd.read_csv("E:/556 a1/dataset4.csv")


# Find the total number of male and female employees
gender_counts = df['Gender'].value_counts()
print('Total number of male employees:', gender_counts['male'])
print('Total number of female employees:', gender_counts['female'])

marital_status_counts = df['Marital Status'].value_counts()
print("Total number of single employees:", marital_status_counts['single'])
print("Total number of married employees:", marital_status_counts['married'])
print("Total number of divorced employees:", marital_status_counts['divorced'])

# df = pd.DataFrame(your_data)

# Filter the DataFrame to get rows where the 'Designation' is 'Manager'

manager_ids = df[df['Designation'] == 'Manager']['Employee ID']


# Print the employee IDs of managers
manager_ids = df[df['Designation'] == 'Manager']['Employee ID']
print("Employee IDs of managers:", manager_ids.tolist())

# Assuming the data is already in a pandas DataFrame called 'df'

# Replace empty records with 0
df = df.fillna(0)

# Assuming the data is already in a pandas DataFrame called 'df'

# Delete rows with any missing values
df = df.dropna()

supervisor_ids = df[df['Designation'] == 'Supervisor']['Employee ID']
print("Employee IDs of supervisors:", supervisor_ids.tolist())

# Filter the DataFrame to get rows where the 'Designation' is 'Manager' and 'City' is 'Pune'
manager_pune_df = df[(df['Designation'] == 'Manager') & (df['City'] == 'Pune')]

# Extract the name of the employee who meets the criteria
employee_name = manager_pune_df['Name']

# Print the name of the employee
print(employee_name)

# Assuming the data is already in a pandas DataFrame called 'df'

# Filter the DataFrame to get rows where the 'Salary' is greater than 100,000
high_salary_df = df[df['Salary'] > 100000]

# Print the details of the employees with salaries greater than 1,00,000/-
print(high_salary_df)