import numpy as np
import matplotlib.pyplot as plt

days = np.array([1, 2, 3, 4, 5, 6, 7])
revenue = np.array([500, 600, 989, 700, 100, 600, 520])
costs = np.array([400, 250, 500, 700, 50, 200, 310])

print("Days:", days)
print("Revenue:", revenue)
print("Costs:", costs)

profit = revenue - costs
print("Profit:", profit)

average_profit = np.mean(profit)
highest_profit = np.max(profit)
lowest_profit = np.min(profit)

print("Average Profit:", average_profit)
print("Highest Profit:", highest_profit)
print("Lowest Profit:", lowest_profit)

plt.plot(days, profit)

plt.title("Daily Business Profit")
plt.xlabel("Day")
plt.ylabel("Profit")
plt.show()
