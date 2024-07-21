import csv

temperatures = []

with open(r"D:\sankhu codes and stuff\angela yu course\python\pandas\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    next(data)  # Skip the header row
    for row in data:
        temperatures.append(int(row[1]))

print(temperatures)
