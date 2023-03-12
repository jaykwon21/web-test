from flask import Flask, render_template
import requests
import json


class weather_information:
    # time, forecast, temperature, chance of rain, humidity, wind speed
    def __init__(self, time, short_forecast, chance_of_rain, humidity, wind_speed, temperature):
        self.time = time
        self.short_forecast = short_forecast
        self.chance_of_rain = chance_of_rain
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.temperature = temperature

    def __str__(self) -> str:
        return str(self.time) + ", " + str(self.short_forecast) + ", " + str(self.chance_of_rain) + ", " + str(self.humidity) + ", " + str(self.wind_speed) + ", " + str(self.temperature)



app = Flask(__name__)

#temperature, probability of precipitation, humidity, wind speed
@app.route('/shortweather')
def shortweatherinformation():
    forecastList = []
    startTimeList = []

    temperature_list = []
    rain_chance_list = []
    humidity_list = []
    wind_speed_list = []

    headers = {
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'text/html; charset=utf-8'
        }
    
    response = requests.get("https://api.weather.gov/gridpoints/BMX/110,46/forecast/hourly", headers=headers)

    data_json = response.json()

    temperatureweather = data_json["properties"]["periods"]

    for forecast in temperatureweather:
        forecastList.append(forecast["shortForecast"])
        startTimeList.append(forecast["startTime"])

        temperature_list.append(forecast["temperature"])
        rain_chance_list.append(forecast["probabilityOfPrecipitation"]['value'])
        humidity_list.append(forecast["relativeHumidity"]['value'])
        wind_speed_list.append(forecast["windSpeed"])


    # print(temperature_list)
    # print(rain_chance_list)
    # print(humidity_list)
    # print(wind_speed_list)


    # startTimeThreeHour = []
    # forecastThreeHour = []

    # temperature_listThreeHour = []
    # rain_chance_listThreeHour = []
    # humidity_listThreeHour = []
    # wind_speed_listThreeHour = []

    # timeAndForecastList = []
    # timeAndForecastDict = {}

    weather_information_instance_list = []

    for i in range(len(forecastList)):
        if i % 3 == 0:
            # forecastThreeHour.append(forecastList[i])

            temp_start_time = startTimeList[i]
            temp_start_time = temp_start_time[8:13]
            temp_short_forecast = forecastList[i]
            temp_temperature = temperature_list[i]
            temp_humidity = humidity_list[i]
            temp_rain_chance = rain_chance_list[i]
            temp_wind_speed = wind_speed_list[i]

            weather_information_instance = weather_information(temp_start_time, temp_short_forecast, temp_rain_chance, temp_humidity, temp_wind_speed, temp_temperature)
            weather_information_instance_list.append(weather_information_instance)


            # startTimeThreeHour.append(tempStartTime)

            # timeAndForecastList.append(tempStartTime + ": " + forecastList[i])
            # timeAndForecastDict[tempStartTime] = forecastList[i]

        else:
            pass
    # print(weather_information_instance_list)
    for info in weather_information_instance_list:
        print(str(info))



    return render_template('class_list_to_table_templates.html', html_list = weather_information_instance_list)


    
def main():
    app.run(debug  = True, port = 8080)
    # weatherinformation()


if __name__ == '__main__':
    main()


shortweatherinformation()