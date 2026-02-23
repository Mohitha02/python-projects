import numpy as np

# Temperature data for 7 days (in Celsius)
temperature = np.array([32, 35, 30, 31, 36, 34, 33])

print("Temperature Data (°C):", temperature)

# Average temperature
avg_temp = np.mean(temperature)
print("Average Temperature:", avg_temp)

# Maximum temperature
max_temp = np.max(temperature)
print("Maximum Temperature:", max_temp)

# Minimum temperature
min_temp = np.min(temperature)
print("Minimum Temperature:", min_temp)

# Days above average temperature
above_avg = temperature[temperature > avg_temp]
print("Days Above Average Temperature:", above_avg)
