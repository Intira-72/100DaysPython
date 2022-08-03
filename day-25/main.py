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

# data = pandas.read_csv("weather_data.csv")

# temp_list = data['temp'].to_list()
# temp_avg = data['temp'].mean()
# temp_max = data.temp.max()

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp * 9/5 + 32)


data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

