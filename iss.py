import requests
import json 

url = 'http://api.open-notify.org/iss-now.json'

req = requests.get(url)

if req.status_code == 200:
    result = json.loads(req.content)
    position =result["iss_position"]
    latitude = position["latitude"]
    longitude = position["longitude"]
    print ("The longitude is {0} and the latitude is {1}".format(longitude, latitude))
elif req.status_code == 404:
    print("Endpoint can't be found")
else:
    print("There is an error")