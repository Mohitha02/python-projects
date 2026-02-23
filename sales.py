import numpy as np

# Sales data for 7 days (in rupees)
sales = np.array([1200, 1500, 1100, 1800, 1700, 1600, 1400])

print("Sales Data:", sales)

# Total sales
total_sales = np.sum(sales)
print("Total Sales:", total_sales)

# Average sales
average_sales = np.mean(sales)
print("Average Sales:", average_sales)

# Maximum sales
max_sales = np.max(sales)
print("Maximum Sales:", max_sales)

# Minimum sales
min_sales = np.min(sales)
print("Minimum Sales:", min_sales)
