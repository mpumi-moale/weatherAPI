# import requests module
import requests

# fetch api key 
api_key = open("api_key.txt", 'r').read()

# name of a city/place
location = input("Enter location: ")

# base url
url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&APPID={api_key}"

# return response object
response = requests.get(url)

# convert json into python format 
weather_data = response.json()

if weather_data["cod"] != "404":

    weather_main = weather_data["main"]
    temperature = weather_main["temp"]
    pressure = weather_main["pressure"]
    humidity = weather_main["humidity"]

    z = weather_data["weather"]
    description = z[0]["description"]

    print(f" Temperature = {temperature} \n description = {description} \nhumidity = {humidity}%")

else:
    print("Location not found") 