import requests
import json
def title():
    url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=c97be7face9fe5e7b9993950f6200a81&language=en-US&page=1&region=ID'
    response =  requests.get(url)
    if response.status_code==200: 
        result = {}
        array = json.loads(response.text)
        for i in range(len(array["results"])):
            if array["results"][i]["backdrop_path"] is not None:
                result[i] = array["results"][i]["original_title"],  array["results"][i]["overview"], "https://image.tmdb.org/t/p/original"+array["results"][i]["backdrop_path"]
        return result
    elif response.status_code==400:
        return "something wrong"
    else:
        return "something wrong, you should try again"

a = title().values()

for i in a:
    print(i)

url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=c97be7face9fe5e7b9993950f6200a81&language=en-US&page=1&region=ID'
response =  requests.get(url)
if response.status_code==200: 
    array = json.loads(response.text)
    print(array)