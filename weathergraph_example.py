import requests
import json
import matplotlib.pyplot as plt

headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }
    

response = requests.get("https://api.weather.gov/gridpoints/BMX/110,46/forecast/hourly", headers=headers)

data_json = response.json()

# print(data_json)

# temperatureweather = str(data_json["properties"]["periods"][0]["temperature"])

weatherForcastInformation = data_json["properties"]["periods"]

# print(weather)

temperatureList = []

for information in weatherForcastInformation:
    temperatureList.append(information["temperature"])

# print(temperatureList)

xValues = []

for i in range(1, 157):
    xValues.append(i)

plt.plot(xValues, temperatureList)
plt.xlabel("Time")
plt.ylabel("Temperatures")
plt.show()
