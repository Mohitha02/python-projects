import numpy as np

# Original product prices
prices = np.array([500, 1200, 750, 300, 1500])

print("Original Prices:", prices)

# 10% discount on all products
discount_10 = prices * 0.10

# Extra 5% discount for products above 1000
extra_discount = np.where(prices > 1000, prices * 0.05, 0)

# Total discount
total_discount = discount_10 + extra_discount

# Final price after discount
final_price = prices - total_discount

print("Total Discount:", total_discount)
print("Final Prices:", final_price)
