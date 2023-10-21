#Import module requests
import requests 
#Creating a key for geting weather
api_key = "0a3a7608680b44ba67f00d8f1ac3bde0"
#ask user city
city_name = input("enter your city: ")
#url for get data from weather
adress = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
# get information from adress(weather)
responce = requests.get(adress)
#check error
if responce.status_code == 200:
    #save data in dict
    data = responce.json()
    #get main data
    main_data = data['main']
    #get temperature from main data
    temperature = main_data['temp']
    #get humidity from main data
    humidity = main_data['humidity']
    #get description from weather
    description = data['weather'][0]['description']
    wind = data['wind']['speed']
    print(f'temperature = {round(temperature - 273.15)} degree')
    print(f'humidity = {humidity}')
    print(f'description = {description}')
    print(f'speed wind = {wind}')
else:
    #addres not found 
    print("city not found")