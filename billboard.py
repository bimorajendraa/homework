import requests
import json

key = 'c97be7face9fe5e7b9993950f6200a81'
def kitsu():
    headers = {'Content-Type': 'application/vnd.api+json'}
    request = requests.get('https://kitsu.io/api/edge/trending/anime', headers=headers)
    response_body = json.loads(request.text)
    result = {}
    for i in response_body['data']:
        result[i['id']] = i['attributes']['titles']['en_jp'], i['attributes']['posterImage']['tiny'], i['attributes']['synopsis']
    return result

def kitsu_image():
    headers = {'Content-Type': 'application/vnd.api+json'}
    request = requests.get('https://kitsu.io/api/edge/trending/anime', headers=headers)
    response_body = json.loads(request.text)

    return response_body

print(kitsu_image())