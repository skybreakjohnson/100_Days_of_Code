import csv

# Füge alle Temperaturen einer Liste hin zu
with open('weather_data.csv') as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        print(row[1])
        # füge jede Reihe, die nicht 'temp' enhält zur Liste ( temperatures ) hin zu
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)
    print(type(temperatures[1]))