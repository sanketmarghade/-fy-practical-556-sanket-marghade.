"""
#What is the total sales for Ragi in Maharashtra?
#How many months are represented in the data?
#Which city has the highest sales in February 2023?
#What is the total sales for Oats in Haryana?
#Which grain has the highest sales in April 2023?
#What is the total sales for Sooji in Tamil Nadu?
#Which grain has the highest sales overall?
#What is the total sales for Brown rice in Telangana?
#How many sales entries are there for Corn?
#What is the total sales for Bajra in Punjab?
#Which city has the highest sales in January 2023?
#What is the total sales for Sattu in Gujarat?
#What is the total sales for Wheat in West Bengal?
#Which grain has the highest sales in May 2023?
#How many sales entries are there for Ragi?
#What is the total sales for Corn in Uttar Pradesh?
#Which city has the highest sales in March 2023?
#What is the total sales for Brown rice in June 2023?
#What is the total sales for Bajra in February 2023?
#Which grain has the highest sales in July 2023?
"""
import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('E:/556 a1/grainsales.csv')

# What is the total sales for Ragi in Maharashtra?
ragi_sales = df.loc[(df['GrainName'] == 'Ragi') & (df['State'] == 'Maharashtra'), 'Sales'].sum()
print("Total sales for Ragi in Maharashtra:", ragi_sales)

# How many months are represented in the data?
months_count = df['Months'].nunique()
print("Number of months represented in the data:", months_count)

# Which city has the highest sales in February 2023?
february_highest_sales = df.loc[df['Months'] == 'FEB', 'Sales'].max()
city_with_highest_sales = df.loc[(df['Months'] == 'FEB') & (df['Sales'] == february_highest_sales), 'City'].iloc[0]
print("City with the highest sales in February 2023:", city_with_highest_sales)

# What is the total sales for Oats in Haryana?
oats_sales = df.loc[(df['GrainName'] == 'Oats') & (df['State'] == 'Hariyana'), 'Sales'].sum()
print("Total sales for Oats in Haryana:", oats_sales)

# Which grain has the highest sales in April 2023?
april_highest_sales = df.loc[df['Months'] == 'APRIL', 'Sales'].max()
grain_with_highest_sales = df.loc[(df['Months'] == 'APRIL') & (df['Sales'] == april_highest_sales), 'GrainName'].iloc[0]
print("Grain with the highest sales in April 2023:", grain_with_highest_sales)

# What is the total sales for Sooji in Tamil Nadu?
sooji_sales = df.loc[(df['GrainName'] == 'Sooji') & (df['State'] == 'Tamil Nadu'), 'Sales'].sum()
print("Total sales for Sooji in Tamil Nadu:", sooji_sales)

# Which grain has the highest sales overall?
grain_highest_sales = df.groupby('GrainName')['Sales'].sum().idxmax()
print("Grain with the highest sales overall:", grain_highest_sales)

# What is the total sales for Brown rice in Telangana?
brown_rice_sales = df.loc[(df['GrainName'] == 'Brown rice') & (df['State'] == 'Telangana'), 'Sales'].sum()
print("Total sales for Brown rice in Telangana:", brown_rice_sales)

# How many sales entries are there for Corn?
corn_entries = df.loc[df['GrainName'] == 'Corn', 'Sales'].count()
print("Number of sales entries for Corn:", corn_entries)

# What is the total sales for Bajra in Punjab?
bajra_sales = df.loc[(df['GrainName'] == 'Bajra') & (df['State'] == 'Panjab'), 'Sales'].sum()
print("Total sales for Bajra in Punjab:", bajra_sales)

# Which city has the highest sales in January 2023?
january_highest_sales = df.loc[df['Months'] == 'JAN', 'Sales'].max()
city_with_highest_sales_january = df.loc[(df['Months'] == 'JAN') & (df['Sales'] == january_highest_sales), 'City'].iloc[0]
print("City with the highest sales in January 2023:", city_with_highest_sales_january)

# What is the total sales for Sattu in Gujarat?
sattu_sales = df.loc[(df['GrainName'] == 'Sattu') & (df['State'] == 'Gujarat'), 'Sales'].sum()
print("Total sales for Sattu in Gujarat:", sattu_sales)

# What is the total sales for Wheat in West Bengal?
wheat_sales = df.loc[(df['GrainName'] == 'Wheat') & (df['State'] == 'West Bengol'), 'Sales'].sum()
print("Total sales for Wheat in West Bengal:", wheat_sales)

# Which grain has the highest sales in May 2023?
may_highest_sales = df.loc[df['Months'] == 'MAY', 'Sales'].max()
grain_with_highest_sales_may = df.loc[(df['Months'] == 'MAY') & (df['Sales'] == may_highest_sales), 'GrainName'].iloc[0]
print("Grain with the highest sales in May 2023:", grain_with_highest_sales_may)

# How many sales entries are there for Ragi?
ragi_entries = df.loc[df['GrainName'] == 'Ragi', 'Sales'].count()
print("Number of sales entries for Ragi:", ragi_entries)

# What is the total sales for Corn in Uttar Pradesh?
corn_sales_up = df.loc[(df['GrainName'] == 'Corn') & (df['State'] == 'UP'), 'Sales'].sum()
print("Total sales for Corn in Uttar Pradesh:", corn_sales_up)

# Which city has the highest sales in March 2023?
march_highest_sales = df.loc[df['Months'] == 'MARCH', 'Sales'].max()
city_with_highest_sales_march = df.loc[(df['Months'] == 'MARCH') & (df['Sales'] == march_highest_sales), 'City'].iloc[0]
print("City with the highest sales in March 2023:", city_with_highest_sales_march)

# What is the total sales for Brown rice in June 2023?
brown_rice_sales_june = df.loc[(df['GrainName'] == 'Brown rice') & (df['Months'] == 'JUNE'), 'Sales'].sum()
print("Total sales for Brown rice in June 2023:", brown_rice_sales_june)

# What is the total sales for Bajra in February 2023?
bajra_sales_feb = df.loc[(df['GrainName'] == 'Bajra') & (df['Months'] == 'FEB'), 'Sales'].sum()
print("Total sales for Bajra in February 2023:", bajra_sales_feb)

# Which grain has the highest sales in July 2023?
july_highest_sales = df.loc[df['Months'] == 'JULY', 'Sales'].max()
grain_with_highest_sales_july = df.loc[(df['Months'] == 'JULY') & (df['Sales'] == july_highest_sales), 'GrainName'].iloc[0]
print("Grain with the highest sales in July 2023:", grain_with_highest_sales_july)
