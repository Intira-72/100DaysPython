# with open("weather_data.csv") as data:
#     print(data.readlines())


# import csv

# with open("weather_data.csv") as data_csv:
#     data = csv.reader(data_csv)
#     temperatures = []

#     for data_row in data:
#         try:
#             temperatures.append(int(data_row[1]))
#         except ValueError:
#             pass

#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
temperatures = list(data['temp'])
print(temperatures)