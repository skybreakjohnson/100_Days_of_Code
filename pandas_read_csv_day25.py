import pandas as pd

data = pd.read_csv('weather_data.csv')

# Zeige alle columns
print(data.columns.values)
print(data.columns)

# Konvertiere DataFrame in ein Dictionary
data_dict = data.to_dict()
print(data_dict)

# Konvertiere Spalte 'temp' in eine Liste
temp_list = data['temp'].to_list()
print(temp_list)
how_many = len(temp_list)

# Durchschnittliche Temperatur ohne sum und pandas ( just for learning purpose :)
temp_all = 0
for i in temp_list:
    temp_all += i
average_temperature = round((temp_all) / len(temp_list), 1)
print(average_temperature)

# Durchschnittliche Temperature mit len und sum
average_temperature = round(sum(temp_list) / len(temp_list), 1)
print(f'The average temperature of all 7 days is: {average_temperature} Degrees Celsius.')

# Durchschnittliche Temperature mit pandas mean()
average_temperature = data['temp'].mean()
print(average_temperature)

# Höchste ( Maximale ) Temperatur
print(data['temp'].max())

# Get Data in Columns
print(data['condition'])
print(data.condition)

# Get Data in Row
print(data[data.day == 'Monday'])

# Tag mit der höchsten Temperatur
print(data[data.temp == data.temp.max()])

# Temperatur von Montag in Fahrenheit
# °F = °C * 1,8 + 32
monday = data[data.day == 'Monday']
monday_fahrenheit = int(monday.temp) * 1.8+ 32
print(monday_fahrenheit)

# Create a dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

df = pd.DataFrame(data_dict)
print(df)

# Schreibe DataFrame in eine csv
df.to_csv('dataframe_from_scratch.csv')