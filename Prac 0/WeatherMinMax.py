#
# Find the minimum and maximum temperatures and dates from temperatures_365_days.csv
#

import csv

# Converts the csv file into a 2xN list
with open('temperatures_365_days.csv') as file:
    reader = csv.reader(file)
    next(reader) # Skips header
    contents = []
    for row in reader:
        tempRow = [row[0], float(row[1])] # Converts the temp into a float
        contents.append(tempRow)

# Min/Max temperature search
tempMax = contents[1][1]
tempMaxDate = contents[1][0]
for i in contents:
    if tempMax <= i[1]:
        tempMax = i[1]
        tempMaxDate = i[0]

tempMin = contents[1][1]
tempMinDate = contents[1][0]
for i in contents:
    if tempMin >= i[1]:
        tempMin = i[1]
        tempMinDate = i[0]

print(f'Hottest day was: {tempMaxDate}, {tempMax} \nColdest day was: {tempMinDate}, {tempMin}')