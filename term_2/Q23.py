# Lists for month names and corresponding number of days
month_names = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Create the dictionary using the two lists
months_days = dict(zip(month_names, days_in_month))

# a. Print all keys in alphabetical order
print("a. All months in alphabetical order:")
for month in sorted(months_days.keys()):
    print(month)

# b. Print key-value pairs sorted by the number of days
print("\nb. Months and their respective days sorted by the number of days:")
sorted_by_days = sorted(months_days.items(), key=lambda x: x[1])
for month, days in sorted_by_days:
    print(f"{month}: {days} days")

# c. Print all months with 31 days
print("\nc. Months with 31 days:")
for month, days in months_days.items():
    if days == 31:
        print(month)
