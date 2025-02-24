#
# Find the minimum and maximum temperatures and dates from temperatures_365_days.csv
#

input = [22, 30, 25, 28, 35, 31, 27]

tempMax = input[0]
for i in input:
    if tempMax <= i:
        tempMax = i

tempMin = input[0]
for i in input:
    if tempMin >= i:
        tempMin = i

print(f'Max temperature is: {tempMax} \nMinimum temperature is: {tempMin}')