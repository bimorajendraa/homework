import json
import requests

def formula(kelvin=0.0):
    cel = kelvin - 273.15 
    return "{0:.1f}".format(cel)

location = input("Location: ")

key = 'bab594a991d0e34bb3dd9fcbb7268a87'
url = 'http://api.openweathermap.org/data/2.5/weather'
payload = {'q': location, 'appid': key}

req = requests.get(url, payload)

if req.status_code == 200:
    result = json.loads(req.content)
    weather = result['weather'][0]['description']
    temp = result['main']
    onecelcius = temp['temp']
    onecelcius = formula(float(onecelcius))
    twocelcius = temp['feels_like']
    twocelcius = formula(float(twocelcius))
    print(f"The weather condition in {location} is {weather}. The temperature is {onecelcius} celcius and it feels like {twocelcius} celcius.")
elif req.status_code == 404:
    print("Endpoint can't be found")
else:
    print("There is an error")
