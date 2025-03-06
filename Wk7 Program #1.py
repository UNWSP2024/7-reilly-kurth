#Reilly Kurth
#3/4/2025

import statistics

rainfall_per_month = []
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for month in months:
    rainfall = float(input(f"Enter total rainfall in {month}:"))
    rainfall_per_month.append(rainfall)

#calculations
total = sum(rainfall_per_month)
print("The total rainfall was", total)
avg = float(statistics.mean(rainfall_per_month))
print("The average rainfall was", avg)
minimum = float(min(rainfall_per_month ))
print("The minimum rainfall was", minimum)
maximum = float(max(rainfall_per_month))
print("The maximum rainfall was", maximum)

#min and max months
max_month = months[rainfall_per_month.index(minimum)]
min_month = months[rainfall_per_month.index(maximum)]

print("The month with the minimum rainfall was", min_month)
print("The month with the maximum rainfall was", max_month)


