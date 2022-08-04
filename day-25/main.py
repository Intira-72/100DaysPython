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


from cmath import nan
import pandas

# data = pandas.read_csv("weather_data.csv")

# temp_list = data['temp'].to_list()
# temp_avg = data['temp'].mean()
# temp_max = data.temp.max()

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp * 9/5 + 32)


# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
color_data = data['Primary Fur Color'].to_list()

color_list = list(set(color_data))[1:]
count_list = [color_data.count(c) for c in color_list]

new_value = {
    'Fur Color': color_list,
    'Count': count_list
}

new_data_csv = pandas.DataFrame(new_value)
new_data_csv.to_csv("squirrel_count.csv")