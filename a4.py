
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("E:/556 a1/grainsales.csv")

# Display the DataFrame
print(df)
# Group by month and calculate total sales
monthly_sales = df.groupby('Months')['Sales'].sum()

#Find the month with the highest sales
best_month = monthly_sales.idxmax()

# Calculate the earnings for the best month
earnings = monthly_sales.max()

# Print the result
print("The best month for sales was", best_month, "with earnings of", earnings)
# Group by grain and calculate total sales
grain_sales = df.groupby('GrainName')['Sales'].sum()

# Find the grain with the highest sales
best_selling_grain = grain_sales.idxmax()

# Print the result
print("The product that sold the most was", best_selling_grain)

# Group by city and calculate total number of products sold
city_sales = df.groupby('City').size()

# Find the city with the highest sales
best_selling_city = city_sales.idxmax()

# Print the result
print("The city that sold the most products was", best_selling_city)

# min income in which month 
earnings = monthly_sales.min()
least_month = monthly_sales.idxmin()
print("The least month for sales was", least_month, "with earnings of", earnings)

#least sell product
least_selling_grain = grain_sales.idxmin()
print("The product that sold the most was", least_selling_grain)


#earning of each states
sales_state=df.groupby('State')['Sales'].sum()
print(sales_state)

#max income of state 
earning=sales_state.max()
state_earnmore=sales_state.idxmax()
print ("state have max  sales earning",state_earnmore,"with earning",earning)

earning=sales_state.min()
state_earnless=sales_state.idxmin()
print ("state have max  sales earning",state_earnless,"with earning",earning)
#Calculate the average sales per city:
average_sales_per_city = df.groupby('City')['Sales'].mean()
print(average_sales_per_city)
#Find the total sales for each state and sort in descending order:
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False)
print(state_sales)

#Filter the data for the month of January:
january_data = df[df['Months'] == 'JAN']
print(january_data)    
