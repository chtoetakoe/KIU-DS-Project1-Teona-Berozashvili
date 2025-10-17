# Project 1 - Task 2: NumPy Arrays & Operations
# Student: Teona Berozashvili
# Honor Code: i certify that this work is my own and i have not plagiarized

import numpy as np


np.random.seed(42)


# Part A: Array Creation & Exploration


#1: temperature data (365 days × 5 cities)
temperature_data= np.random.uniform(-10.0,40.0,(365,5))
print("=== TEMPERATURE DATA ===")
print("Shape:",temperature_data.shape)
print("Dimensions:",temperature_data.ndim)
print("data type:",temperature_data.dtype)
print("size:",temperature_data.size)
print()

#2:sales matrix (12 months × 4 product categories)
sales_matrix=np.random.randint(1000,5000,(12,4))

print("=== SALES MATRIX ===")
print(sales_matrix)
print("shape:", sales_matrix.shape)
print()

# 3:special arrays
identity_matrix=np.eye(5)
evenly_spaced=np.linspace(0, 100,50)

print("=== SPECIAL ARRAYS ===")
print("Identity Matrix:\n", identity_matrix)
print()
print("Evenly Spaced Values:\n", evenly_spaced)
print()


#Part B: Array Manipulation & Indexing 


# 1:basic slicing
january=temperature_data[:31, :]
summer=temperature_data[151:243, :]
weekend=temperature_data[4::7, :]
print("january data shape:",january.shape)
print("summer data shape:",summer.shape)
print("weekend data shape:",weekend.shape)
print()


# 2:boolean indexing
hotd=np.any(temperature_data>35,axis=1)
hot_days=temperature_data[hotd]
print("Days with temp > 35°C:",hot_days.shape[0])

freezing_days_per_city=np.sum(temperature_data<0,axis=0)
print("freezing days per city:",freezing_days_per_city)

comfortablem =(temperature_data>= 15) & (temperature_data<=25)
comfortable_days=np.sum(comfortablem)
print("total comfortable readings:",comfortable_days)

temperature_data[temperature_data< -5] = -5
print("Cleaned temperature data (values below -5 replaced).")
print()


#3:fancy indexing
selected_days=temperature_data[[0, 100, 200, 300, 364], :]
print("Selected days data:\n", selected_days)

quarterly_avgs = [
    np.mean(temperature_data[0:91, :], axis=0),
    np.mean(temperature_data[91:182, :], axis=0),
    np.mean(temperature_data[182:273, :], axis=0),
    np.mean(temperature_data[273:, :], axis=0)
]
quarterly_avgs = np.array(quarterly_avgs)
print("\nQuarterly averages shape:", quarterly_avgs.shape)

city_avg = np.mean(temperature_data, axis=0)
sorted_indices = np.argsort(city_avg)[::-1]
reordered_data = temperature_data[:, sorted_indices]
print("Cities rearranged by avg temp (descending).")
print()




# PART C: MATHEMATICAL OPERATIONS & STATISTICS


#1:temperature analysis

mean=np.mean(temperature_data,axis=0)
median=np.median(temperature_data,axis=0)
std=np.std(temperature_data,axis=0)
print("mean per city:",mean)
print("median per city:",median)
print("Std per city:",std)

hottest_day=np.unravel_index(np.argmax(temperature_data),temperature_data.shape)
coldest_day=np.unravel_index(np.argmin(temperature_data),temperature_data.shape)
print("\nhottest day:", hottest_day, "temp:", temperature_data[hottest_day])
print("coldest day:", coldest_day, "temp:", temperature_data[coldest_day])

temp_range= np.max(temperature_data, axis=0) - np.min(temperature_data,axis=0)
print("temperature range:",temp_range)

city_correlation = np.corrcoef(temperature_data, rowvar=False)
print("\ncorrelation between cities:\n", city_correlation)
print()



#2:sales analysis
total_sales_per_category = np.sum(sales_matrix, axis=0)
avg_sales_per_category = np.mean(sales_matrix, axis=0)
monthly_totals = np.sum(sales_matrix, axis=1)
best_month = np.argmax(monthly_totals) + 1
best_category = np.argmax(total_sales_per_category) + 1

print("Total sales per category:", total_sales_per_category)
print("Avg monthly sales per category:", avg_sales_per_category)
print("Best month overall:", best_month)
print("Best category overall:", best_category)
print()

#3:advanced computations
moving_7= np.convolve(np.mean(temperature_data, axis=1), np.ones(7)/7, mode='valid')
print("7-day moving average length:", moving_7.shape[0])

z_scores = (temperature_data - mean) / std
print("Z-scores shape:", z_scores.shape)

percentiles_25 = np.percentile(temperature_data, 25, axis=0)
percentiles_50 = np.percentile(temperature_data, 50, axis=0)
percentiles_75 = np.percentile(temperature_data, 75, axis=0)
print("\n25th percentiles:", percentiles_25)
print("50th percentiles:", percentiles_50)
print("75th percentiles:", percentiles_75)
print()
